extends SceneTree

func _init():
	var pack = load("res://Scenes/UI/character_menu.tscn")
	var root = pack.instantiate()
	
	var panel = root.get_node("Panel")
	if panel:
		# Set anchor to Bottom Left
		panel.set_anchors_preset(Control.PRESET_BOTTOM_LEFT)
		
		panel.grow_horizontal = Control.GROW_DIRECTION_END
		panel.grow_vertical = Control.GROW_DIRECTION_BEGIN
		
		# Offset dari sudut kiri bawah
		panel.offset_left = 20
		panel.offset_bottom = -20
		panel.offset_right = 620
		panel.offset_top = -520
		
	var new_pack = PackedScene.new()
	new_pack.pack(root)
	ResourceSaver.save(new_pack, "res://Scenes/UI/character_menu.tscn")
	
	print("Fixed position!")
	quit()
