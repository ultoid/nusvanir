extends CanvasLayer

@onready var btn_buy = $Panel/TopBar/BtnBuy
@onready var btn_sell = $Panel/TopBar/BtnSell
@onready var btn_cancel = $Panel/TopBar/BtnCancel

@onready var item_vbox = $Panel/HBox/LeftPanel/ScrollContainer/VBoxContainer
@onready var lbl_coins = $Panel/HBox/RightPanel/LblCoins
@onready var lbl_possession = $Panel/HBox/RightPanel/LblPossession

var current_mode = "BUY"

func _ready():
	process_mode = Node.PROCESS_MODE_ALWAYS
	
	btn_buy.pressed.connect(func(): _set_mode("BUY"))
	btn_sell.pressed.connect(func(): _set_mode("SELL"))
	btn_cancel.pressed.connect(_close_menu)
	
	_set_mode("BUY")

func _set_mode(mode: String):
	current_mode = mode
	_update_ui()

func _update_ui():
	# Bersihkan list
	for child in item_vbox.get_children():
		child.queue_free()
		
	if not get_node_or_null("/root/ItemDB"): return
	
	var shop_items = ["potion", "ether"]
	
	for item_id in shop_items:
		var item_data = ItemDB.get_item(item_id)
		if item_data.is_empty(): continue
		
		var btn = Button.new()
		var price = item_data.get("price", 0)
		var sell_price = int(price / 2)
		var item_name = item_data.get("name", "Unknown")
		
		if current_mode == "BUY":
			btn.text = "%s - %d Koin" % [item_name, price]
			if get_node_or_null("/root/Global") and Global.coins < price:
				btn.disabled = true
			btn.pressed.connect(func(id=item_id): _on_item_pressed(id))
		elif current_mode == "SELL":
			btn.text = "Jual %s - %d Koin" % [item_name, sell_price]
			if get_node_or_null("/root/Global") and Global.inventory.get(item_id, 0) <= 0:
				btn.disabled = true
			btn.pressed.connect(func(id=item_id): _on_item_pressed(id))
			
		item_vbox.add_child(btn)
	
	if get_node_or_null("/root/Global"):
		lbl_coins.text = "Koin: " + str(Global.coins) + " G"
		var pot_count = Global.inventory.get("potion", 0)
		var eth_count = Global.inventory.get("ether", 0)
		lbl_possession.text = "Dimiliki: Potion (%d), Ether (%d)" % [pot_count, eth_count]

func _on_item_pressed(item_id: String):
	if not get_node_or_null("/root/Global") or not get_node_or_null("/root/ItemDB"): return
	
	var item_data = ItemDB.get_item(item_id)
	var price = item_data.get("price", 0)
	var sell_price = int(price / 2)
	
	if current_mode == "BUY":
		if Global.coins >= price:
			Global.coins -= price
			Global.inventory[item_id] = Global.inventory.get(item_id, 0) + 1
			_sync_player_coins()
	elif current_mode == "SELL":
		if Global.inventory.get(item_id, 0) > 0:
			Global.inventory[item_id] -= 1
			Global.coins += sell_price
			_sync_player_coins()
			
	_update_ui()

func _sync_player_coins():
	var players = get_tree().get_nodes_in_group("Player")
	if players.size() > 0:
		players[0].coins = Global.coins
		players[0].emit_signal("coin_changed", Global.coins)

func _close_menu():
	get_tree().paused = false
	queue_free()
