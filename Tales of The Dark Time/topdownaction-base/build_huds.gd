extends SceneTree

func _init():
	print("Building HUD Scenes...")
	
	# 1. PLAYER HUD
	var player_hud = CanvasLayer.new()
	player_hud.name = "PlayerHUD"
	
	# Bars
	var hp_bar = ProgressBar.new()
	hp_bar.name = "HealthBar"
	hp_bar.modulate = Color(1, 0, 0)
	hp_bar.position = Vector2(25, 21)
	hp_bar.size = Vector2(300, 27)
	hp_bar.show_percentage = false
	player_hud.add_child(hp_bar)
	hp_bar.owner = player_hud
	
	var ep_bar = ProgressBar.new()
	ep_bar.name = "EnergyBar"
	ep_bar.modulate = Color(1, 1, 0)
	ep_bar.position = Vector2(25, 52)
	ep_bar.size = Vector2(300, 13)
	ep_bar.show_percentage = false
	player_hud.add_child(ep_bar)
	ep_bar.owner = player_hud
	
	var mp_bar = ProgressBar.new()
	mp_bar.name = "ManaBar"
	mp_bar.modulate = Color(0, 0.5, 1)
	mp_bar.position = Vector2(25, 68)
	mp_bar.size = Vector2(300, 13)
	mp_bar.show_percentage = false
	player_hud.add_child(mp_bar)
	mp_bar.owner = player_hud
	
	var coin_lbl = Label.new()
	coin_lbl.name = "CoinLabel"
	coin_lbl.position = Vector2(25, 85)
	coin_lbl.text = "0 G"
	player_hud.add_child(coin_lbl)
	coin_lbl.owner = player_hud
	
	# Exp
	var exp_bar = ProgressBar.new()
	exp_bar.name = "ExpBar"
	exp_bar.position = Vector2(4, 708)
	exp_bar.size = Vector2(1268, 12)
	exp_bar.show_percentage = false
	player_hud.add_child(exp_bar)
	exp_bar.owner = player_hud
	
	var lvl_lbl = Label.new()
	lvl_lbl.name = "LevelLabel"
	lvl_lbl.position = Vector2(12, 679)
	lvl_lbl.text = "Lv.1"
	player_hud.add_child(lvl_lbl)
	lvl_lbl.owner = player_hud
	
	# Skills HBox
	var skill_box = HBoxContainer.new()
	skill_box.name = "SkillBox"
	skill_box.position = Vector2(500, 650)
	player_hud.add_child(skill_box)
	skill_box.owner = player_hud
	for i in range(1, 5):
		var p = Panel.new()
		p.custom_minimum_size = Vector2(50, 50)
		p.name = "Skill" + str(i)
		
		var l = Label.new()
		l.text = str(i)
		l.set_anchors_preset(Control.PRESET_BOTTOM_RIGHT)
		p.add_child(l)
		l.owner = player_hud
		
		skill_box.add_child(p)
		p.owner = player_hud
		
	# Items HBox
	var item_box = HBoxContainer.new()
	item_box.name = "ItemBox"
	item_box.position = Vector2(750, 650)
	player_hud.add_child(item_box)
	item_box.owner = player_hud
	for i in range(1, 3):
		var p = Panel.new()
		p.custom_minimum_size = Vector2(50, 50)
		p.name = "Item" + str(i)
		
		var item_lbl = Label.new()
		item_lbl.name = "ItemLabel"
		item_lbl.text = ""
		item_lbl.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
		item_lbl.set_anchors_preset(Control.PRESET_FULL_RECT)
		p.add_child(item_lbl)
		item_lbl.owner = player_hud
		
		var l = Label.new()
		l.text = str(i+4)
		l.set_anchors_preset(Control.PRESET_BOTTOM_RIGHT)
		p.add_child(l)
		l.owner = player_hud
		
		item_box.add_child(p)
		p.owner = player_hud
		
	var pack_player = PackedScene.new()
	pack_player.pack(player_hud)
	ResourceSaver.save(pack_player, "res://Scenes/UI/player_hud.tscn")
	
	# 2. BOSS HUD
	var boss_hud = CanvasLayer.new()
	boss_hud.name = "BossHUD"
	
	var bhp_bar = ProgressBar.new()
	bhp_bar.name = "BossHealthBar"
	bhp_bar.modulate = Color(1, 0, 0)
	bhp_bar.position = Vector2(300, 20)
	bhp_bar.size = Vector2(680, 30)
	bhp_bar.show_percentage = false
	boss_hud.add_child(bhp_bar)
	bhp_bar.owner = boss_hud
	
	var bname_lbl = Label.new()
	bname_lbl.name = "BossNameLabel"
	bname_lbl.position = Vector2(300, -2)
	bname_lbl.size = Vector2(680, 23)
	bname_lbl.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	bname_lbl.text = "BOSS"
	boss_hud.add_child(bname_lbl)
	bname_lbl.owner = boss_hud
	
	var pack_boss = PackedScene.new()
	pack_boss.pack(boss_hud)
	ResourceSaver.save(pack_boss, "res://Scenes/UI/boss_hud.tscn")
	
	# 3. GAME OVER HUD
	var go_hud = CanvasLayer.new()
	go_hud.name = "GameOverHUD"
	
	var panel = Panel.new()
	panel.name = "Panel"
	panel.position = Vector2(373, 204)
	panel.size = Vector2(503, 299)
	go_hud.add_child(panel)
	panel.owner = go_hud
	
	var title = Label.new()
	title.text = "GAME OVER"
	title.position = Vector2(200, 20)
	panel.add_child(title)
	title.owner = go_hud
	
	var sum_lbl = Label.new()
	sum_lbl.name = "SummaryLabel"
	sum_lbl.position = Vector2(50, 60)
	sum_lbl.size = Vector2(400, 100)
	sum_lbl.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	sum_lbl.text = "Summary"
	panel.add_child(sum_lbl)
	sum_lbl.owner = go_hud
	
	var btn_respawn = Button.new()
	btn_respawn.name = "BtnRespawn"
	btn_respawn.text = "Kembali ke Kota"
	btn_respawn.position = Vector2(100, 200)
	panel.add_child(btn_respawn)
	btn_respawn.owner = go_hud
	
	var btn_resurrect = Button.new()
	btn_resurrect.name = "BtnResurrect"
	btn_resurrect.text = "Bangkit Kembali (100 G)"
	btn_resurrect.position = Vector2(250, 200)
	panel.add_child(btn_resurrect)
	btn_resurrect.owner = go_hud
	
	var pack_go = PackedScene.new()
	pack_go.pack(go_hud)
	ResourceSaver.save(pack_go, "res://Scenes/UI/game_over_hud.tscn")
	
	print("Done!")
	quit()
