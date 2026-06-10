extends CanvasLayer

var player_ref: Node2D = null

@onready var grid = get_node_or_null("Panel/Grid")
@onready var btn_close = get_node_or_null("Panel/BtnClose")
@onready var popup = get_node_or_null("SkillPopup")

var current_selected_skill: String = ""

func _ready():
	process_mode = Node.PROCESS_MODE_ALWAYS
	
	if btn_close:
		btn_close.pressed.connect(_close_menu)
		
	if popup:
		popup.clear()
		popup.add_item("Pasang ke Slot 1", 0)
		popup.add_item("Pasang ke Slot 2", 1)
		popup.add_item("Pasang ke Slot 3", 2)
		popup.add_item("Pasang ke Slot 4", 3)
		popup.add_item("Lepas dari Slot", 4)
		popup.add_item("Batal", 5)
		popup.id_pressed.connect(_on_popup_pressed)

func setup(p: Node2D):
	player_ref = p
	_refresh_skills()

func _refresh_skills():
	if not grid: return
	
	for child in grid.get_children():
		child.queue_free()
		
	if not get_node_or_null("/root/Global") or not get_node_or_null("/root/SkillDB"): return
	
	var all_skills = SkillDB.skills.keys()
	
	# Anggap 18 slot grid
	for i in range(18):
		var btn = Button.new()
		btn.custom_minimum_size = Vector2(100, 100)
		
		if i < all_skills.size():
			var skill_id = all_skills[i]
			var data = SkillDB.get_skill(skill_id)
			
			var is_unlocked = Global.unlocked_skills.has(skill_id)
			var lvl_req = data.get("req_level", 1)
			
			if is_unlocked:
				btn.text = data["name"] + "\n[UNLOCKED]"
				btn.modulate = Color(1, 1, 1)
			else:
				btn.text = data["name"] + "\n[Lv." + str(lvl_req) + "]"
				btn.modulate = Color(0.5, 0.5, 0.5)
				
			btn.add_theme_font_size_override("font_size", 12)
			btn.pressed.connect(_on_skill_click.bind(skill_id, is_unlocked, lvl_req))
		else:
			btn.disabled = true
			
		grid.add_child(btn)

func _on_skill_click(skill_id: String, is_unlocked: bool, lvl_req: int):
	if is_unlocked:
		current_selected_skill = skill_id
		if popup:
			popup.position = Vector2(get_viewport().get_mouse_position().x, get_viewport().get_mouse_position().y)
			popup.popup()
	else:
		if player_ref and player_ref.level >= lvl_req:
			Global.unlocked_skills.append(skill_id)
			_refresh_skills()
		else:
			if player_ref and player_ref.has_method("spawn_floating_text"):
				player_ref.spawn_floating_text("Level tidak cukup!", Color(1, 0, 0))

func _on_popup_pressed(id: int):
	if current_selected_skill == "" or not get_node_or_null("/root/Global"): return
	
	if id >= 0 and id <= 3: # Slot 1, 2, 3, 4
		Global.quick_skills[id] = current_selected_skill
		_update_hud()
	elif id == 4: # Lepas
		for i in range(4):
			if Global.quick_skills[i] == current_selected_skill:
				Global.quick_skills[i] = ""
		_update_hud()
	elif id == 5: # Batal
		pass

func _update_hud():
	var hud = get_tree().current_scene.get_node_or_null("PlayerHUD")
	if hud and hud.has_method("_update_quick_skills"):
		hud._update_quick_skills()

func _close_menu():
	get_tree().paused = false
	queue_free()

func _unhandled_key_input(event):
	if event.is_action_pressed("open_skill_menu"):
		_close_menu()
		get_viewport().set_input_as_handled()
