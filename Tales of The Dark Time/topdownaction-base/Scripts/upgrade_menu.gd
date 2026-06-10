extends CanvasLayer

var player: Node2D

# Buff Shop System
var all_buffs = [
	{"id": "speed", "title": "Sepatu Hermes", "desc": "Lari +20%", "cost": 10},
	{"id": "damage", "title": "Otot Kawat", "desc": "Damage Dasar +2", "cost": 15},
	{"id": "health", "title": "Darah Suci", "desc": "Max HP +50", "cost": 15},
	{"id": "atk_speed", "title": "Tangan Kilat", "desc": "Atk Speed +20%", "cost": 10}
]
var shop_buffs = []

# Temp Stats System
var temp_points: int = 0
var temp_str: int = 0
var temp_agi: int = 0
var temp_vit: int = 0

@onready var lbl_str = $Panel/HBoxContainer/StatPanel/VBox/RowSTR/LblVal
@onready var btn_str_up = $Panel/HBoxContainer/StatPanel/VBox/RowSTR/BtnUp
@onready var btn_str_dn = $Panel/HBoxContainer/StatPanel/VBox/RowSTR/BtnDn

@onready var lbl_agi = $Panel/HBoxContainer/StatPanel/VBox/RowAGI/LblVal
@onready var btn_agi_up = $Panel/HBoxContainer/StatPanel/VBox/RowAGI/BtnUp
@onready var btn_agi_dn = $Panel/HBoxContainer/StatPanel/VBox/RowAGI/BtnDn

@onready var lbl_vit = $Panel/HBoxContainer/StatPanel/VBox/RowVIT/LblVal
@onready var btn_vit_up = $Panel/HBoxContainer/StatPanel/VBox/RowVIT/BtnUp
@onready var btn_vit_dn = $Panel/HBoxContainer/StatPanel/VBox/RowVIT/BtnDn

@onready var lbl_points = $Panel/HBoxContainer/StatPanel/VBox/PointsRow/LblPoints
@onready var btn_confirm = $Panel/HBoxContainer/StatPanel/VBox/BtnConfirm
@onready var btn_close = $Panel/BtnClose

# Shop nodes
@onready var shop_btn1 = $Panel/HBoxContainer/ShopPanel/VBox/ShopBtn1
@onready var shop_btn2 = $Panel/HBoxContainer/ShopPanel/VBox/ShopBtn2
@onready var shop_btn3 = $Panel/HBoxContainer/ShopPanel/VBox/ShopBtn3
@onready var lbl_coins = $Panel/HBoxContainer/ShopPanel/VBox/LblCoins

func _ready():
	process_mode = Node.PROCESS_MODE_ALWAYS
	
	btn_str_up.pressed.connect(func(): _change_stat("STR", 1))
	btn_str_dn.pressed.connect(func(): _change_stat("STR", -1))
	btn_agi_up.pressed.connect(func(): _change_stat("AGI", 1))
	btn_agi_dn.pressed.connect(func(): _change_stat("AGI", -1))
	btn_vit_up.pressed.connect(func(): _change_stat("VIT", 1))
	btn_vit_dn.pressed.connect(func(): _change_stat("VIT", -1))
	
	btn_confirm.pressed.connect(_confirm_stats)
	btn_close.pressed.connect(_close_menu)
	
	shop_btn1.pressed.connect(func(): _buy_buff(0))
	shop_btn2.pressed.connect(func(): _buy_buff(1))
	shop_btn3.pressed.connect(func(): _buy_buff(2))

func setup(player_node: Node2D):
	player = player_node
	
	# Load current stats
	temp_points = player.stat_points
	temp_str = player.stat_str
	temp_agi = player.stat_agi
	temp_vit = player.stat_vit
	
	# Roll Shop Buffs
	var shuffled_buffs = all_buffs.duplicate()
	shuffled_buffs.shuffle()
	shop_buffs = [shuffled_buffs[0], shuffled_buffs[1], shuffled_buffs[2]]
	
	_update_ui()

func _update_ui():
	# Update Stats UI
	lbl_str.text = "%02d" % temp_str
	lbl_agi.text = "%02d" % temp_agi
	lbl_vit.text = "%02d" % temp_vit
	lbl_points.text = "%02d" % temp_points
	
	btn_str_up.disabled = temp_points <= 0
	btn_agi_up.disabled = temp_points <= 0
	btn_vit_up.disabled = temp_points <= 0
	
	btn_str_dn.disabled = temp_str <= player.stat_str
	btn_agi_dn.disabled = temp_agi <= player.stat_agi
	btn_vit_dn.disabled = temp_vit <= player.stat_vit
	
	btn_confirm.disabled = temp_points == player.stat_points
	
	# Update Shop UI
	lbl_coins.text = "Koin Anda: " + str(player.coins)
	_update_shop_button(shop_btn1, 0)
	_update_shop_button(shop_btn2, 1)
	_update_shop_button(shop_btn3, 2)

func _update_shop_button(btn: Button, index: int):
	var b = shop_buffs[index]
	btn.text = b["title"] + " (" + str(b["cost"]) + " Koin)\n" + b["desc"]
	btn.disabled = player.coins < b["cost"]

func _change_stat(stat_name: String, amount: int):
	if amount > 0 and temp_points <= 0: return
	
	if stat_name == "STR":
		if amount < 0 and temp_str <= player.stat_str: return
		temp_str += amount
	elif stat_name == "AGI":
		if amount < 0 and temp_agi <= player.stat_agi: return
		temp_agi += amount
	elif stat_name == "VIT":
		if amount < 0 and temp_vit <= player.stat_vit: return
		temp_vit += amount
		
	temp_points -= amount
	_update_ui()

func _confirm_stats():
	player.stat_str = temp_str
	player.stat_agi = temp_agi
	player.stat_vit = temp_vit
	player.stat_points = temp_points
	player.recalculate_stats()
	print("Stat dikonfirmasi! Sisa Poin: ", player.stat_points)
	_update_ui()

func _buy_buff(index: int):
	var b = shop_buffs[index]
	if player.coins < b["cost"]: return
	
	player.coins -= b["cost"]
	player.emit_signal("coin_changed", player.coins)
	
	# Terapkan efek permanen
	if b["id"] == "speed":
		player.walk_speed *= 1.2
		player.run_speed *= 1.2
	elif b["id"] == "damage":
		player.base_damage += 2 # Karena pedang mengambil rumus base_damage
	elif b["id"] == "health":
		player.max_health += 50
		player.current_health = min(player.current_health + 50, player.max_health)
		player.emit_signal("health_changed", player.current_health, player.max_health)
	elif b["id"] == "atk_speed":
		player.attack_speed_multiplier *= 1.2
		
	print("Buff berhasil dibeli: ", b["title"])
	_update_ui()

func _close_menu():
	get_tree().paused = false
	queue_free()
