extends Area2D

var hit_enemies = []

func _ready():
	# Memastikan Area2D ini bisa mendeteksi tabrakan
	body_entered.connect(_on_body_entered)
	area_entered.connect(_on_area_entered)

func clear_hit_list():
	hit_enemies.clear()

func _on_body_entered(body):
	if body.is_in_group("Enemy"):
		_deal_damage(body)

func _on_area_entered(area):
	var parent = area.get_parent()
	if parent and parent.is_in_group("Enemy"):
		_deal_damage(parent)

func _deal_damage(enemy_node):
	if enemy_node in hit_enemies:
		return # Mencegah damage ganda
	hit_enemies.append(enemy_node)
	
	if enemy_node.has_method("take_damage"):
		var player = get_parent()
		var current_damage = 10
		if player and "current_attack_damage" in player:
			current_damage = player.current_attack_damage
			
		enemy_node.take_damage(current_damage, global_position)
