extends SceneTree

func _init():
	print("Building Inventory Menu...")
	
	var inv_menu = CanvasLayer.new()
	inv_menu.name = "InventoryMenu"
	
	var panel = Panel.new()
	panel.name = "Panel"
	panel.size = Vector2(800, 600)
	panel.position = Vector2((1280 - 800) / 2.0, (720 - 600) / 2.0)
	inv_menu.add_child(panel)
	panel.owner = inv_menu
	
	var title = Label.new()
	title.name = "Title"
	title.text = "INVENTORY"
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.position = Vector2(0, 20)
	title.size = Vector2(800, 30)
	panel.add_child(title)
	title.owner = inv_menu
	
	var grid = GridContainer.new()
	grid.name = "Grid"
	grid.columns = 8
	grid.position = Vector2(50, 80)
	grid.add_theme_constant_override("h_separation", 10)
	grid.add_theme_constant_override("v_separation", 10)
	panel.add_child(grid)
	grid.owner = inv_menu
	
	var btn_close = Button.new()
	btn_close.name = "BtnClose"
	btn_close.text = "Tutup (B)"
	btn_close.position = Vector2(350, 520)
	btn_close.size = Vector2(100, 40)
	panel.add_child(btn_close)
	btn_close.owner = inv_menu
	
	var popup = PopupMenu.new()
	popup.name = "ItemPopup"
	inv_menu.add_child(popup)
	popup.owner = inv_menu
	
	var pack = PackedScene.new()
	pack.pack(inv_menu)
	ResourceSaver.save(pack, "res://Scenes/UI/inventory_menu.tscn")
	
	print("Done Inventory!")
	quit()
