extends CharacterBody2D

@export var speed: float = 70.0
@export var max_health: int = 5
@export var damage: int = 1

@export var chase_radius: float = 300.0
@export var ideal_min_dist: float = 120.0
@export var ideal_max_dist: float = 200.0

var current_health: int
var knockback_velocity: Vector2 = Vector2.ZERO

var is_chasing: bool = false
var spawn_position: Vector2
var shoot_timer: float = 0.0

var player: Node2D

@onready var sprite = $Sprite2D
@onready var projectile_scene = preload("res://Scenes/Skills/enemy_projectile.tscn")

func _ready():
	current_health = max_health
	spawn_position = global_position
	add_to_group("Enemy")
	
	var players = get_tree().get_nodes_in_group("Player")
	if players.size() > 0:
		player = players[0]

func _physics_process(delta):
	if knockback_velocity != Vector2.ZERO:
		velocity = knockback_velocity
		knockback_velocity = knockback_velocity.lerp(Vector2.ZERO, 0.1)
		if knockback_velocity.length() < 10:
			knockback_velocity = Vector2.ZERO
		move_and_slide()
		return
		
	if player and not player.is_dead:
		var dist = global_position.distance_to(player.global_position)
		
		if dist <= chase_radius:
			is_chasing = true
		elif dist > chase_radius + 100:
			is_chasing = false
			
		if is_chasing:
			var dir = (player.global_position - global_position).normalized()
			
			# Kiting Logic
			if dist > ideal_max_dist:
				velocity = dir * speed # Kejar jika terlalu jauh
			elif dist < ideal_min_dist:
				velocity = -dir * speed # Mundur jika terlalu dekat
			else:
				velocity = Vector2.ZERO # Berhenti jika jarak ideal
				
			if velocity.x != 0:
				sprite.flip_h = velocity.x < 0
				
			# Shooting Logic
			shoot_timer -= delta
			if shoot_timer <= 0:
				shoot_projectile(dir)
				shoot_timer = 2.0
		else:
			# Kembali ke posisi awal jika player kabur
			if global_position.distance_to(spawn_position) > 10:
				var dir = (spawn_position - global_position).normalized()
				velocity = dir * speed
				if velocity.x != 0:
					sprite.flip_h = velocity.x < 0
			else:
				velocity = Vector2.ZERO
				
	move_and_slide()

func shoot_projectile(dir: Vector2):
	if not projectile_scene: return
	
	var proj = projectile_scene.instantiate()
	proj.global_position = global_position
	proj.direction = dir
	proj.z_index = 5
	get_tree().current_scene.call_deferred("add_child", proj)
	print("Ranged Enemy menembak!")

# Melee contact (in case player touches them)
func _on_hurtbox_body_entered(body):
	if body.is_in_group("Player") and body.has_method("take_damage"):
		body.take_damage(damage, global_position)
		knockback_velocity = (global_position - body.global_position).normalized() * 150.0

func take_damage(amount: int, knockback_source: Vector2 = Vector2.ZERO):
	current_health -= amount
	spawn_damage_text(amount, Color(1, 1, 1))
	
	if knockback_source != Vector2.ZERO:
		var knockback_direction = (global_position - knockback_source).normalized()
		knockback_velocity = knockback_direction * 200.0
	
	modulate = Color(1, 0, 0)
	await get_tree().create_timer(0.1).timeout
	modulate = Color(1, 1, 1)
	
	if current_health <= 0:
		if player and not player.is_dead:
			player.enemies_killed += 1
		drop_loot()
		queue_free()

func drop_loot():
	if randf() > 0.5:
		var coin_scene = load("res://Scenes/Items/coin.tscn")
		if coin_scene:
			var coin = coin_scene.instantiate()
			coin.global_position = global_position
			get_tree().current_scene.call_deferred("add_child", coin)
			
	var exp_scene = load("res://Scenes/Items/exp_gem.tscn")
	if exp_scene:
		var exp_gem = exp_scene.instantiate()
		exp_gem.global_position = global_position
		get_tree().current_scene.call_deferred("add_child", exp_gem)

func spawn_damage_text(amount: int, color: Color):
	var label = Label.new()
	label.text = str(amount)
	label.modulate = color
	label.global_position = global_position + Vector2(randf_range(-10, 10), -20)
	
	get_tree().current_scene.add_child(label)
	
	var tween = label.create_tween()
	tween.tween_property(label, "global_position", label.global_position + Vector2(0, -30), 0.5)
	tween.parallel().tween_property(label, "modulate:a", 0.0, 0.5)
	tween.tween_callback(label.queue_free)
