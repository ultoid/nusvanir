extends StaticBody2D

@export var npc_name: String = "Penduduk"
@export_multiline var dialogue_lines: Array[String] = ["Halo, selamat datang di kota kami!"]
@export_enum("Talk", "Merchant", "Portal") var npc_type: String = "Talk"

var player_in_range = false
var dialogue_box_scene = preload("res://Scenes/UI/dialogue_box.tscn")
var current_dialogue_box = null

func _ready():
	$Label.text = npc_name
	if has_node("InteractArea"):
		$InteractArea.body_entered.connect(_on_body_entered)
		$InteractArea.body_exited.connect(_on_body_exited)

func _on_body_entered(body):
	if body.is_in_group("Player"):
		player_in_range = true

func _on_body_exited(body):
	if body.is_in_group("Player"):
		player_in_range = false

func _process(_delta):
	if player_in_range and Input.is_action_just_pressed("interact"):
		if current_dialogue_box == null or not is_instance_valid(current_dialogue_box):
			interact()

func interact():
	current_dialogue_box = dialogue_box_scene.instantiate()
	get_tree().current_scene.add_child(current_dialogue_box)
	
	if npc_type == "Talk":
		current_dialogue_box.start_dialogue(dialogue_lines)
	elif npc_type == "Merchant":
		current_dialogue_box.start_dialogue(dialogue_lines, self, "open_shop")
	elif npc_type == "Portal":
		current_dialogue_box.start_dialogue(dialogue_lines, self, "warp_to_dungeon")

func open_shop():
	var shop_scene = load("res://Scenes/UI/shop_menu.tscn")
	if shop_scene:
		var shop = shop_scene.instantiate()
		get_tree().current_scene.add_child(shop)
		get_tree().paused = true
			
func warp_to_dungeon():
	if get_node_or_null("/root/Global"):
		Global.reset_dungeon_run()
	get_tree().change_scene_to_file("res://Scenes/Maps/dungeon_2.tscn")
