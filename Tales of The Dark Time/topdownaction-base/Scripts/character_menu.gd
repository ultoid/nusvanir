extends CanvasLayer

var player: Node2D

var temp_points: int = 0
var temp_stats = {
	"STR": 0, "VIT": 0, "INT": 0, "LUK": 0, "AGI": 0, "DEX": 0
}

var lbl_points: Label
@onready var btn_confirm = $Panel/MainVBox/BtnConfirm
@onready var btn_close = $Panel/BtnClose

var ui_stats = {}
var ui_details = {}

var equip_popup: PopupMenu
var current_clicked_slot: String = ""

func _ready():
	process_mode = Node.PROCESS_MODE_ALWAYS
	
	# Node bisa dicari secara dinamis karena strukturnya rumit
	var stats_grid = find_child("StatsGrid", true, false)
	if stats_grid:
		for stat in ["STR", "VIT", "INT", "LUK", "AGI", "DEX"]:
			var btn_up = stats_grid.get_node("BtnUp" + stat)
			var btn_dn = stats_grid.get_node("BtnDn" + stat)
			var lbl_val = stats_grid.get_node("Val" + stat)
			
			ui_stats[stat] = {
				"btn_up": btn_up,
				"btn_dn": btn_dn,
				"lbl_val": lbl_val
			}
			
			btn_up.pressed.connect(func(): _change_stat(stat, 1))
			btn_dn.pressed.connect(func(): _change_stat(stat, -1))
			
	var detail_grid = find_child("DetailGrid", true, false)
	if detail_grid:
		for d in ["MaxHP", "MaxMP", "Atk", "Matk", "Def", "Mdef", "Hit", "Flee", "Critical", "Aspd"]:
			ui_details[d] = detail_grid.get_node("Detail" + d)
			
	# Hubungkan tombol equipment
	for slot in ["Weapon", "Armor", "Accessory"]:
		var btn = find_child("Btn" + slot, true, false)
		if btn:
			btn.pressed.connect(func(): _on_slot_clicked(slot.to_lower()))
			
	equip_popup = PopupMenu.new()
	equip_popup.add_item("Lepas", 0)
	equip_popup.add_item("Batal", 1)
	equip_popup.id_pressed.connect(_on_equip_popup_pressed)
	add_child(equip_popup)
			
	# Perbaiki LblPoints yang lokasinya di StatHeader
	var stat_header = find_child("LblPoints", true, false)
	if stat_header:
		lbl_points = stat_header
		
	if btn_confirm: btn_confirm.pressed.connect(_confirm_stats)
	if btn_close: btn_close.pressed.connect(_close_menu)

func setup(player_node: Node2D):
	player = player_node
	
	temp_points = player.stat_points
	temp_stats["STR"] = player.stat_str
	temp_stats["VIT"] = player.stat_vit
	temp_stats["INT"] = player.stat_int
	temp_stats["LUK"] = player.stat_luk
	temp_stats["AGI"] = player.stat_agi
	temp_stats["DEX"] = player.stat_dex
	
	_update_ui()
	_update_equipment_ui()

func _update_equipment_ui():
	var item_db = get_node_or_null("/root/ItemDB")
	for slot in ["Weapon", "Armor", "Accessory"]:
		var btn = find_child("Btn" + slot, true, false)
		if not btn: continue
		var item_id = Global.equipment[slot.to_lower()]
		if item_id == "":
			btn.text = "Kosong"
		else:
			if item_db:
				var data = item_db.get_item(item_id)
				btn.text = data.get("name", item_id.capitalize())
			else:
				btn.text = item_id

func _on_slot_clicked(slot: String):
	if Global.equipment[slot] == "": return
	
	current_clicked_slot = slot
	equip_popup.position = Vector2(get_viewport().get_mouse_position().x, get_viewport().get_mouse_position().y)
	equip_popup.popup()

func _on_equip_popup_pressed(id: int):
	if id == 0: # Lepas
		_unequip_item(current_clicked_slot)
	current_clicked_slot = ""

func _unequip_item(slot: String):
	var item_id = Global.equipment[slot]
	if item_id == "": return
	
	Global.equipment[slot] = ""
	if not Global.inventory.has(item_id):
		Global.inventory[item_id] = 0
	Global.inventory[item_id] += 1
	
	if player.has_method("recalculate_stats"):
		player.recalculate_stats()
		if player.has_node("PlayerHUD"):
			player.get_node("PlayerHUD")._update_hp_mp_ep()
			
	_update_equipment_ui()
	_update_ui()

func _update_ui():
	if lbl_points: lbl_points.text = "Sisa Stat Point: %02d" % temp_points
	
	var bonuses = {}
	if player.has_method("get_equipment_bonuses"):
		bonuses = player.get_equipment_bonuses()
		
	for stat in temp_stats.keys():
		var bns = bonuses.get(stat.to_lower(), 0)
		ui_stats[stat]["lbl_val"].text = "%d + %d" % [temp_stats[stat], bns]
		ui_stats[stat]["btn_up"].disabled = temp_points <= 0
		ui_stats[stat]["btn_dn"].disabled = temp_stats[stat] <= player.get("stat_" + stat.to_lower())
		
	var t_str = temp_stats["STR"] + bonuses.get("str", 0)
	var t_vit = temp_stats["VIT"] + bonuses.get("vit", 0)
	var t_int = temp_stats["INT"] + bonuses.get("int", 0)
	var t_luk = temp_stats["LUK"] + bonuses.get("luk", 0)
	var t_agi = temp_stats["AGI"] + bonuses.get("agi", 0)
	var t_dex = temp_stats["DEX"] + bonuses.get("dex", 0)
		
	var sim_hp = 50 + (t_vit * 10) + bonuses.get("max_hp", 0)
	var sim_mp = 20 + (t_int * 5) + bonuses.get("max_mp", 0)
	var sim_p_atk = 10 + (t_str * 2) + bonuses.get("p_atk", 0)
	var sim_m_atk = 10 + (t_int * 2) + bonuses.get("m_atk", 0)
	var sim_p_def = t_vit + bonuses.get("p_def", 0)
	var sim_m_def = int(t_vit / 2.0 + t_int / 2.0) + bonuses.get("m_def", 0)
	var sim_spd = 80.0 + (t_agi * 4.0)
	var sim_crit = t_luk * 1.0
	
	if ui_details.has("MaxHP"): ui_details["MaxHP"].text = str(sim_hp)
	if ui_details.has("MaxMP"): ui_details["MaxMP"].text = str(sim_mp)
	if ui_details.has("Atk"): ui_details["Atk"].text = str(sim_p_atk)
	if ui_details.has("Matk"): ui_details["Matk"].text = str(sim_m_atk)
	if ui_details.has("Def"): ui_details["Def"].text = str(sim_p_def)
	if ui_details.has("Mdef"): ui_details["Mdef"].text = str(sim_m_def)
	if ui_details.has("Hit"): ui_details["Hit"].text = str(t_dex * 2)
	if ui_details.has("Flee"): ui_details["Flee"].text = str(t_agi * 2)
	if ui_details.has("Critical"): ui_details["Critical"].text = "%.1f%%" % sim_crit
	if ui_details.has("Aspd"): ui_details["Aspd"].text = str(sim_spd)
	
	if btn_confirm: btn_confirm.disabled = temp_points == player.stat_points
	

func _change_stat(stat_name: String, amount: int):
	if amount > 0 and temp_points <= 0: return
	
	var current_base = player.get("stat_" + stat_name.to_lower())
	if amount < 0 and temp_stats[stat_name] <= current_base: return
	
	temp_stats[stat_name] += amount
	temp_points -= amount
	_update_ui()

func _confirm_stats():
	player.stat_str = temp_stats["STR"]
	player.stat_vit = temp_stats["VIT"]
	player.stat_int = temp_stats["INT"]
	player.stat_luk = temp_stats["LUK"]
	player.stat_agi = temp_stats["AGI"]
	player.stat_dex = temp_stats["DEX"]
	player.stat_points = temp_points
	
	player.recalculate_stats()
	_update_ui()

func _close_menu():
	get_tree().paused = false
	queue_free()

func _unhandled_key_input(event):
	if event.is_action_pressed("open_menu"):
		_close_menu()
		get_viewport().set_input_as_handled()
