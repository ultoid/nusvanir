extends Node

var skills = {
	"heal": {
		"name": "Heal",
		"description": "Memulihkan 20 HP. Membutuhkan 10 MP.",
		"req_level": 2,
		"mp_cost": 10,
		"cast_time": 3.0, # Base cast time dalam detik
		"effect_amount": 20,
		"type": "instant",
		"icon_color": Color(0.2, 0.8, 0.2)
	},
	"fireball": {
		"name": "Fireball",
		"description": "Menembakkan bola api ke area target. Membutuhkan 20 MP.",
		"req_level": 1,
		"mp_cost": 20,
		"cast_time": 3.0,
		"type": "target_aoe",
		"range": 100, # Jarak maksimal dari player
		"aoe_radius": 15, # Besarnya ledakan
		"effect_multiplier": 1.5, # Damage = magic_attack * multiplier
		"icon_color": Color(0.9, 0.3, 0.1)
	}
}

func get_skill(id: String) -> Dictionary:
	if skills.has(id):
		return skills[id]
	return {}
