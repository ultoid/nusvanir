extends CanvasLayer

var player_ref: Node2D = null

@onready var grid = get_node_or_null("Panel/Grid")
@onready var btn_close = get_node_or_null("Panel/BtnClose")
@onready var popup = get_node_or_null("ItemPopup")

var current_selected_item: String = ""

func _ready():
	process_mode = Node.PROCESS_MODE_ALWAYS
	
	if btn_close:
		btn_close.pressed.connect(_close_menu)
		
	if popup:
		popup.id_pressed.connect(_on_popup_pressed)

func setup(p: Node2D):
	player_ref = p
	_refresh_inventory()

func _refresh_inventory():
	if not grid: return
	
	for child in grid.get_children():
		child.queue_free()
		
	if not get_node_or_null("/root/Global"): return
	
	var items = []
	for item_id in Global.inventory.keys():
		var count = Global.inventory[item_id]
		if count > 0:
			items.append({"id": item_id, "count": count})
			
	var item_db = get_node_or_null("/root/ItemDB")
	
	for i in range(24): # 3 rows of 8
		var btn = Button.new()
		btn.custom_minimum_size = Vector2(80, 80)
		
		if i < items.size():
			var item = items[i]
			var item_name = item.id.substr(0, 3).capitalize()
			if item_db:
				var data = item_db.get_item(item.id)
				if data and data.has("name"):
					item_name = data["name"].substr(0, 3)
					
			btn.text = item_name + "\nx" + str(item.count)
			btn.add_theme_font_size_override("font_size", 14)
			btn.pressed.connect(_on_item_click.bind(item.id))
		else:
			btn.disabled = true
			
		grid.add_child(btn)

func _on_item_click(item_id: String):
	current_selected_item = item_id
	if popup:
		popup.clear()
		
		var is_equip = false
		var item_db = get_node_or_null("/root/ItemDB")
		if item_db:
			var data = item_db.get_item(item_id)
			var type = data.get("type", "consumable")
			if type in ["weapon", "armor", "accessory"]:
				is_equip = true
				
		if is_equip:
			popup.add_item("Pakai", 0)
			popup.add_item("Buang", 3)
		else:
			popup.add_item("Gunakan", 0)
			popup.add_item("Set Quickslot 5", 1)
			popup.add_item("Set Quickslot 6", 2)
			popup.add_item("Buang", 3)
			
		popup.position = Vector2(get_viewport().get_mouse_position().x, get_viewport().get_mouse_position().y)
		popup.popup()

func _on_popup_pressed(id: int):
	if current_selected_item == "" or not get_node_or_null("/root/Global"): return
	
	var item_db = get_node_or_null("/root/ItemDB")
	var data = {}
	if item_db: data = item_db.get_item(current_selected_item)
	var type = data.get("type", "consumable")
	
	if id == 0: # Gunakan / Pakai
		if type in ["weapon", "armor", "accessory"]:
			var old_equip = Global.equipment[type]
			if old_equip != "":
				if not Global.inventory.has(old_equip):
					Global.inventory[old_equip] = 0
				Global.inventory[old_equip] += 1
				
			Global.equipment[type] = current_selected_item
			Global.inventory[current_selected_item] -= 1
			
			if player_ref and player_ref.has_method("recalculate_stats"):
				player_ref.recalculate_stats()
				if player_ref.has_node("PlayerHUD"):
					player_ref.get_node("PlayerHUD")._update_hp_mp_ep()
		else:
			if player_ref and player_ref.has_method("_use_quick_item"):
				var old = Global.quick_items[0]
				Global.quick_items[0] = current_selected_item
				player_ref._use_quick_item(0)
				Global.quick_items[0] = old
			
	elif id == 1: # Quickslot 5
		Global.quick_items[0] = current_selected_item
		_update_hud()
	elif id == 2: # Quickslot 6
		Global.quick_items[1] = current_selected_item
		_update_hud()
	elif id == 3: # Buang
		Global.inventory[current_selected_item] -= 1
		
	_refresh_inventory()

func _update_hud():
	var hud = get_tree().current_scene.get_node_or_null("PlayerHUD")
	if hud and hud.has_method("_update_quick_items"):
		hud._update_quick_items()

func _close_menu():
	get_tree().paused = false
	queue_free()

func _unhandled_key_input(event):
	if event.is_action_pressed("open_inventory"):
		_close_menu()
		get_viewport().set_input_as_handled()
