extends SceneTree

func _init():
	var root = CanvasLayer.new()
	root.name = "CharacterMenu"
	
	var panel = Panel.new()
	panel.name = "Panel"
	panel.custom_minimum_size = Vector2(600, 500)
	panel.set_anchors_preset(Control.PRESET_BOTTOM_LEFT)
	panel.grow_horizontal = Control.GROW_DIRECTION_END
	panel.grow_vertical = Control.GROW_DIRECTION_BEGIN
	panel.offset_left = 20
	panel.offset_bottom = -20
	panel.offset_right = 620
	panel.offset_top = -520
	root.add_child(panel)
	panel.owner = root
	
	var main_vbox = VBoxContainer.new()
	main_vbox.name = "MainVBox"
	main_vbox.set_anchors_preset(Control.PRESET_FULL_RECT)
	main_vbox.offset_left = 10
	main_vbox.offset_top = 10
	main_vbox.offset_right = -10
	main_vbox.offset_bottom = -10
	panel.add_child(main_vbox)
	main_vbox.owner = root
	
	var equip_label = Label.new()
	equip_label.name = "TitleEquip"
	equip_label.text = "Equipment"
	equip_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	main_vbox.add_child(equip_label)
	equip_label.owner = root
	
	var equip_hbox = HBoxContainer.new()
	equip_hbox.name = "EquipHBox"
	equip_hbox.alignment = BoxContainer.ALIGNMENT_CENTER
	equip_hbox.size_flags_vertical = Control.SIZE_EXPAND_FILL
	main_vbox.add_child(equip_hbox)
	equip_hbox.owner = root
	
	var equip_left = VBoxContainer.new()
	equip_left.name = "EquipLeft"
	equip_left.alignment = BoxContainer.ALIGNMENT_CENTER
	equip_left.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	equip_hbox.add_child(equip_left)
	equip_left.owner = root
	
	for slot in ["Weapon", "Armor"]:
		var hb = HBoxContainer.new()
		hb.name = "Slot" + slot
		hb.alignment = BoxContainer.ALIGNMENT_END
		equip_left.add_child(hb)
		hb.owner = root
		
		var lbl = Label.new()
		lbl.text = slot
		lbl.custom_minimum_size = Vector2(80, 0)
		hb.add_child(lbl)
		lbl.owner = root
		
		var btn = Button.new()
		btn.name = "Btn" + slot
		btn.text = "Kosong"
		btn.custom_minimum_size = Vector2(150, 40)
		hb.add_child(btn)
		btn.owner = root
		
	var center_preview = ColorRect.new()
	center_preview.name = "Preview"
	center_preview.color = Color(0.1, 0.1, 0.1, 0.5)
	center_preview.custom_minimum_size = Vector2(120, 180)
	equip_hbox.add_child(center_preview)
	center_preview.owner = root
	
	var lbl_preview = Label.new()
	lbl_preview.text = "Player"
	lbl_preview.set_anchors_preset(Control.PRESET_CENTER)
	center_preview.add_child(lbl_preview)
	lbl_preview.owner = root
	
	var equip_right = VBoxContainer.new()
	equip_right.name = "EquipRight"
	equip_right.alignment = BoxContainer.ALIGNMENT_CENTER
	equip_right.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	equip_hbox.add_child(equip_right)
	equip_right.owner = root
	
	for slot in ["Accessory"]:
		var hb = HBoxContainer.new()
		hb.name = "Slot" + slot
		hb.alignment = BoxContainer.ALIGNMENT_BEGIN
		equip_right.add_child(hb)
		hb.owner = root
		
		var btn = Button.new()
		btn.name = "Btn" + slot
		btn.text = "Kosong"
		btn.custom_minimum_size = Vector2(150, 40)
		hb.add_child(btn)
		btn.owner = root
		
		var lbl = Label.new()
		lbl.text = slot
		lbl.custom_minimum_size = Vector2(80, 0)
		hb.add_child(lbl)
		lbl.owner = root
		
	var hs = HSeparator.new()
	main_vbox.add_child(hs)
	hs.owner = root
	
	# === BOTTOM SECTION: STATS ===
	var stat_header = HBoxContainer.new()
	main_vbox.add_child(stat_header)
	stat_header.owner = root
	
	var title_stat = Label.new()
	title_stat.text = "Status"
	stat_header.add_child(title_stat)
	title_stat.owner = root
	
	var lbl_points = Label.new()
	lbl_points.name = "LblPoints"
	lbl_points.text = "Sisa Stat Point: 0"
	lbl_points.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	lbl_points.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
	stat_header.add_child(lbl_points)
	lbl_points.owner = root
	
	var stat_hbox = HBoxContainer.new()
	stat_hbox.name = "StatHBox"
	stat_hbox.size_flags_vertical = Control.SIZE_EXPAND_FILL
	main_vbox.add_child(stat_hbox)
	stat_hbox.owner = root
	
	var stats_grid = GridContainer.new()
	stats_grid.name = "StatsGrid"
	stats_grid.columns = 5
	stats_grid.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	stat_hbox.add_child(stats_grid)
	stats_grid.owner = root
	
	var stats = ["STR", "AGI", "VIT", "INT", "DEX", "LUK"]
	for stat in stats:
		var lbl_name = Label.new()
		lbl_name.text = stat
		lbl_name.custom_minimum_size = Vector2(40, 0)
		stats_grid.add_child(lbl_name)
		lbl_name.owner = root
		
		var lbl_val = Label.new()
		lbl_val.name = "Val" + stat
		lbl_val.text = "1 + 0"
		lbl_val.custom_minimum_size = Vector2(60, 0)
		stats_grid.add_child(lbl_val)
		lbl_val.owner = root
		
		var btn_up = Button.new()
		btn_up.name = "BtnUp" + stat
		btn_up.text = "+"
		stats_grid.add_child(btn_up)
		btn_up.owner = root
		
		var btn_dn = Button.new()
		btn_dn.name = "BtnDn" + stat
		btn_dn.text = "-"
		stats_grid.add_child(btn_dn)
		btn_dn.owner = root
		
		var padding = Control.new()
		padding.custom_minimum_size = Vector2(20, 0)
		stats_grid.add_child(padding)
		padding.owner = root
		
	var vs = VSeparator.new()
	stat_hbox.add_child(vs)
	vs.owner = root
	
	var detail_grid = GridContainer.new()
	detail_grid.name = "DetailGrid"
	detail_grid.columns = 4
	detail_grid.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	stat_hbox.add_child(detail_grid)
	detail_grid.owner = root
	
	# We will populate detail_grid dynamically in code or we can just pre-create Labels
	var details = ["MaxHP", "MaxMP", "Atk", "Matk", "Def", "Mdef", "Hit", "Flee", "Critical", "Aspd"]
	for d in details:
		var lbl_n = Label.new()
		lbl_n.text = d
		lbl_n.custom_minimum_size = Vector2(60, 0)
		detail_grid.add_child(lbl_n)
		lbl_n.owner = root
		
		var lbl_v = Label.new()
		lbl_v.name = "Detail" + d
		lbl_v.text = "0 + 0"
		lbl_v.custom_minimum_size = Vector2(60, 0)
		detail_grid.add_child(lbl_v)
		lbl_v.owner = root
	
	var btn_confirm = Button.new()
	btn_confirm.name = "BtnConfirm"
	btn_confirm.text = "Terapkan Stat"
	main_vbox.add_child(btn_confirm)
	btn_confirm.owner = root
	
	var btn_close = Button.new()
	btn_close.name = "BtnClose"
	btn_close.text = "X"
	btn_close.position = Vector2(560, 10)
	btn_close.size = Vector2(30, 30)
	panel.add_child(btn_close)
	btn_close.owner = root
	
	var script = load("res://Scripts/character_menu.gd")
	root.set_script(script)
	
	var pack = PackedScene.new()
	pack.pack(root)
	ResourceSaver.save(pack, "res://Scenes/UI/character_menu.tscn")
	
	print("Character Menu Saved!")
	quit()
