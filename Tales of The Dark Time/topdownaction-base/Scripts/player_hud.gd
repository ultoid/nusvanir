extends CanvasLayer

var player_ref: Node = null

@onready var health_bar = get_node_or_null("HealthBar")
@onready var energy_bar = get_node_or_null("EnergyBar")
@onready var mana_bar = get_node_or_null("ManaBar")
@onready var coin_label = get_node_or_null("CoinLabel")
@onready var exp_bar = get_node_or_null("ExpBar")
@onready var level_label = get_node_or_null("LevelLabel")

@onready var dash_cooldown_rect = get_node_or_null("DashIcon/DashCooldown")
@onready var heavy_cooldown_rect = get_node_or_null("HeavyIcon/HeavyCooldown")

var quick_item_labels = []
var quick_skill_labels = []

func _ready():
	var boss_bar = get_node_or_null("BossHealthBar")
	if boss_bar: boss_bar.queue_free()
	var boss_label = get_node_or_null("BossNameLabel")
	if boss_label: boss_label.queue_free()
	var game_over = get_node_or_null("GameOverPanel")
	if game_over: game_over.queue_free()
	var potion_icon = get_node_or_null("PotionIcon")
	if potion_icon: potion_icon.queue_free()
	
	_setup_quickslots()
	
	var players = get_tree().get_nodes_in_group("Player")
	if players.size() > 0:
		player_ref = players[0]
		player_ref.health_changed.connect(_on_health_changed)
		player_ref.energy_changed.connect(_on_energy_changed)
		player_ref.mana_changed.connect(_on_mana_changed)
		player_ref.coin_changed.connect(_on_coin_changed)
		player_ref.exp_changed.connect(_on_exp_changed)
		
		_on_health_changed(player_ref.current_health, player_ref.max_health)
		_on_energy_changed(player_ref.current_energy, player_ref.max_energy)
		_on_mana_changed(player_ref.current_mana, player_ref.max_mana)
		_on_coin_changed(player_ref.coins)
		_on_exp_changed(player_ref.current_exp, player_ref.max_exp, player_ref.level)

func _setup_quickslots():
	# Skill Slots
	for i in range(4):
		var rect = ColorRect.new()
		rect.color = Color(0.1, 0.1, 0.1, 0.8)
		rect.size = Vector2(40, 40)
		rect.position = Vector2(800 + (i * 45), 650)
		
		var lbl = Label.new()
		lbl.text = str(i + 1)
		lbl.set_anchors_preset(Control.PRESET_BOTTOM_RIGHT)
		lbl.position = Vector2(25, 20)
		rect.add_child(lbl)
		
		var skill_lbl = Label.new()
		skill_lbl.set_anchors_preset(Control.PRESET_FULL_RECT)
		skill_lbl.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
		skill_lbl.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
		skill_lbl.add_theme_font_size_override("font_size", 10)
		rect.add_child(skill_lbl)
		quick_skill_labels.append(skill_lbl)
		
		add_child(rect)
		
	# Item Slots
	for i in range(2):
		var rect = ColorRect.new()
		rect.color = Color(0.2, 0.4, 0.2, 0.8)
		rect.size = Vector2(40, 40)
		rect.position = Vector2(1000 + (i * 45), 650)
		
		var item_lbl = Label.new()
		item_lbl.set_anchors_preset(Control.PRESET_FULL_RECT)
		item_lbl.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
		item_lbl.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
		item_lbl.add_theme_font_size_override("font_size", 10)
		rect.add_child(item_lbl)
		quick_item_labels.append(item_lbl)
		
		var lbl = Label.new()
		lbl.text = str(i + 5)
		lbl.set_anchors_preset(Control.PRESET_BOTTOM_RIGHT)
		lbl.position = Vector2(25, 20)
		rect.add_child(lbl)
		
		add_child(rect)

func _process(delta):
	if player_ref:
		if dash_cooldown_rect:
			if player_ref.current_dash_cooldown > 0:
				var p = player_ref.current_dash_cooldown / player_ref.dash_cooldown
				dash_cooldown_rect.size.y = p * 50.0
			else:
				dash_cooldown_rect.size.y = 0
				
		if heavy_cooldown_rect:
			if player_ref.charge_attack_cooldown > 0:
				var p = player_ref.charge_attack_cooldown / 2.0
				heavy_cooldown_rect.size.y = p * 50.0
			else:
				heavy_cooldown_rect.size.y = 0
	
	_update_quick_items()
	_update_quick_skills()

func _update_quick_items():
	if not get_node_or_null("/root/Global"): return
	var item_db = get_node_or_null("/root/ItemDB")
	
	for i in range(2):
		var item_id = Global.quick_items[i]
		if item_id == "" or Global.inventory.get(item_id, 0) <= 0:
			quick_item_labels[i].text = ""
		else:
			var count = Global.inventory.get(item_id, 0)
			var item_name = item_id.substr(0, 3).capitalize()
			if item_db:
				var data = item_db.get_item(item_id)
				if data and data.has("name"):
					item_name = data["name"].substr(0, 3)
			quick_item_labels[i].text = item_name + "\nx" + str(count)

func _update_quick_skills():
	if not get_node_or_null("/root/Global"): return
	var skill_db = get_node_or_null("/root/SkillDB")
	
	for i in range(4):
		var skill_id = Global.quick_skills[i]
		if skill_id == "":
			quick_skill_labels[i].text = ""
		else:
			var skill_name = skill_id.substr(0, 3).capitalize()
			if skill_db:
				var data = skill_db.get_skill(skill_id)
				if data and data.has("name"):
					skill_name = data["name"].substr(0, 3)
			quick_skill_labels[i].text = skill_name

func _on_health_changed(current: int, maximum: int):
	if health_bar:
		health_bar.max_value = maximum
		health_bar.value = current

func _on_mana_changed(current: int, maximum: int):
	if mana_bar:
		mana_bar.max_value = maximum
		mana_bar.value = current

func _on_energy_changed(current: float, maximum: float):
	if energy_bar:
		energy_bar.max_value = maximum
		energy_bar.value = current

func _on_coin_changed(coins: int):
	if coin_label: coin_label.text = str(coins)

func _on_exp_changed(current: int, maximum: int, level: int):
	if exp_bar:
		exp_bar.max_value = maximum
		exp_bar.value = current
	if level_label:
		level_label.text = "Lv." + str(level)
