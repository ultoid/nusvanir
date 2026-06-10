extends Node

var coins: int = 0
var level: int = 1
var current_exp: int = 0
var max_exp: int = 10

# Stats Permanen dari Town
var perm_stat_str: int = 5
var perm_stat_vit: int = 5
var perm_stat_int: int = 5
var perm_stat_luk: int = 5
var perm_stat_agi: int = 5
var perm_stat_dex: int = 5

# Inventory Dictionary [item_id: jumlah]
var inventory: Dictionary = {
	"potion": 5,
	"ether": 5,
	"iron_sword": 1,
	"leather_armor": 1,
	"ruby_ring": 1
}

var equipment: Dictionary = {
	"weapon": "",
	"armor": "",
	"accessory": ""
}

var quick_items = ["", ""] # item_id slot 1 dan 2

var unlocked_skills: Array = ["heal", "fireball"] # ID skill yang sudah dipelajari
var quick_skills = ["", "", "", ""] # skill slot 1, 2, 3, 4


func _ready():
	_setup_inputs()

func _setup_inputs():
	var inputs = {
		"move_up": KEY_W,
		"move_down": KEY_S,
		"move_left": KEY_A,
		"move_right": KEY_D,
		"run": KEY_SHIFT,
		"jump": KEY_SPACE,
		"interact": KEY_Q,
		"open_menu": KEY_C,
		"open_inventory": KEY_B,
		"open_skill_menu": KEY_K,
		"skill_1": KEY_1,
		"skill_2": KEY_2,
		"skill_3": KEY_3,
		"skill_4": KEY_4,
		"item_1": KEY_5,
		"item_2": KEY_6
	}
	
	for action in inputs.keys():
		if not InputMap.has_action(action):
			InputMap.add_action(action)
		var ev = InputEventKey.new()
		ev.physical_keycode = inputs[action]
		InputMap.action_add_event(action, ev)
		
	# Mouse inputs
	if not InputMap.has_action("basic_attack"):
		InputMap.add_action("basic_attack")
		var ev_left = InputEventMouseButton.new()
		ev_left.button_index = MOUSE_BUTTON_LEFT
		InputMap.action_add_event("basic_attack", ev_left)
		
	if not InputMap.has_action("charge_attack"):
		InputMap.add_action("charge_attack")
		var ev_right = InputEventMouseButton.new()
		ev_right.button_index = MOUSE_BUTTON_RIGHT
		InputMap.action_add_event("charge_attack", ev_right)

func reset_dungeon_run():
	# Dipanggil setiap kali mati
	# Koin, level, exp, dan perm_stats TIDAK direset!
	pass
