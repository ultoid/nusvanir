extends Node

var items = {
	"potion": {
		"name": "Potion",
		"description": "Menyembuhkan 50 HP.",
		"type": "consumable",
		"price": 10,
		"effect_type": "heal_hp",
		"effect_amount": 50
	},
	"ether": {
		"name": "Ether",
		"description": "Menyembuhkan 20 MP.",
		"type": "consumable",
		"price": 20,
		"effect_type": "heal_mp",
		"effect_amount": 20
	},
	"iron_sword": {
		"name": "Iron Sword",
		"description": "Pedang besi standar.",
		"type": "weapon",
		"price": 150,
		"bonus_p_atk": 15,
		"bonus_str": 2
	},
	"leather_armor": {
		"name": "Leather Armor",
		"description": "Baju zirah ringan dari kulit.",
		"type": "armor",
		"price": 120,
		"bonus_p_def": 5,
		"bonus_max_hp": 30
	},
	"ruby_ring": {
		"name": "Ruby Ring",
		"description": "Cincin yang memancarkan energi magis.",
		"type": "accessory",
		"price": 200,
		"bonus_int": 4,
		"bonus_max_mp": 10
	}
}

func get_item(item_id: String) -> Dictionary:
	if items.has(item_id):
		return items[item_id]
	return {}
