extends CharacterBody2D

signal boss_health_changed(current, maximum)
signal boss_died

@export var speed: float = 60.0
@export var max_health: int = 200
@export var damage: int = 3
@export var chase_radius: float = 800.0

var current_health: int
var knockback_velocity: Vector2 = Vector2.ZERO

var is_chasing: bool = false
var shoot_timer: float = 0.0
var state: String = "CHASE" # CHASE atau SHOOT

var player: Node2D

@onready var sprite = $Sprite2D
@onready var projectile_scene = preload("res://Scenes/Skills/enemy_projectile.tscn")

func _ready():
	current_health = max_health
	add_to_group("Enemy")
	
	var players = get_tree().get_nodes_in_group("Player")
	if players.size() > 0:
		player = players[0]
		
	_update_hud()

func _update_hud():
	var hud = get_tree().current_scene.get_node_or_null("HUD")
	if hud and hud.has_method("update_boss_health"):
		hud.update_boss_health(current_health, max_health)

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
		elif dist > chase_radius + 200:
			is_chasing = false
			
		if is_chasing:
			shoot_timer -= delta
			
			if state == "CHASE":
				var dir = (player.global_position - global_position).normalized()
				velocity = dir * speed
				if velocity.x != 0:
					sprite.flip_h = velocity.x < 0
					
				# Berhenti dan tembak setiap 4 detik
				if shoot_timer <= 0:
					state = "SHOOT"
					velocity = Vector2.ZERO
					shoot_timer = 1.0 # Waktu diam saat menembak
					call_deferred("shoot_bullet_hell")
			
			elif state == "SHOOT":
				# Diam di tempat selama 1 detik (animasi menembak)
				velocity = Vector2.ZERO
				if shoot_timer <= 0:
					state = "CHASE"
					shoot_timer = 4.0 # Kembali mengejar selama 4 detik
		else:
			velocity = Vector2.ZERO
				
	move_and_slide()

func shoot_bullet_hell():
	if not projectile_scene: return
	print("Boss mengeluarkan Bullet Hell 8 Arah!")
	
	var num_bullets = 8
	for i in range(num_bullets):
		var angle = (PI * 2 / num_bullets) * i
		var dir = Vector2(cos(angle), sin(angle))
		
		var proj = projectile_scene.instantiate()
		proj.global_position = global_position
		proj.direction = dir
		proj.z_index = 5
		get_tree().current_scene.call_deferred("add_child", proj)

func _on_hurtbox_body_entered(body):
	if body.is_in_group("Player") and body.has_method("take_damage"):
		body.take_damage(damage, global_position)
		knockback_velocity = (global_position - body.global_position).normalized() * 300.0

func take_damage(amount: int, knockback_source: Vector2 = Vector2.ZERO):
	current_health -= amount
	_update_hud()
	
	spawn_damage_text(amount, Color(1, 0.84, 0)) # Warna Emas untuk damage ke boss
	
	if knockback_source != Vector2.ZERO:
		var knockback_direction = (global_position - knockback_source).normalized()
		knockback_velocity = knockback_direction * 50.0 # Boss susah dipantulkan
	
	modulate = Color(1, 0, 0)
	await get_tree().create_timer(0.1).timeout
	modulate = Color(1, 0.5, 0.5) # Kembali ke warna aslinya
	
	if current_health <= 0:
		var hud = get_tree().current_scene.get_node_or_null("HUD")
		if hud and hud.has_method("hide_boss_health"):
			hud.hide_boss_health()
			
		if player and not player.is_dead:
			player.enemies_killed += 1
			
		# Panggil UI Hadiah Boss (Buff Shop)
		var buff_shop_scene = load("res://Scenes/UI/buff_shop_menu.tscn")
		if buff_shop_scene:
			var shop = buff_shop_scene.instantiate()
			# Tambahkan ke parent tertinggi agar tidak ikut hancur saat boss queue_free
			get_tree().current_scene.add_child(shop)
			shop.setup(player)
			
		emit_signal("boss_died")
		drop_loot()
		queue_free()

func drop_loot():
	# Boss menjatuhkan banyak hadiah
	for i in range(5):
		var coin_scene = load("res://Scenes/Items/coin.tscn")
		if coin_scene:
			var coin = coin_scene.instantiate()
			coin.global_position = global_position + Vector2(randf_range(-20, 20), randf_range(-20, 20))
			get_tree().current_scene.call_deferred("add_child", coin)
			
	for i in range(3):
		var exp_scene = load("res://Scenes/Items/exp_gem.tscn")
		if exp_scene:
			var exp_gem = exp_scene.instantiate()
			exp_gem.global_position = global_position + Vector2(randf_range(-20, 20), randf_range(-20, 20))
			get_tree().current_scene.call_deferred("add_child", exp_gem)

func spawn_damage_text(amount: int, color: Color):
	var label = Label.new()
	label.text = str(amount)
	label.modulate = color
	label.global_position = global_position + Vector2(randf_range(-20, 20), -40)
	
	get_tree().current_scene.add_child(label)
	
	var tween = label.create_tween()
	tween.tween_property(label, "global_position", label.global_position + Vector2(0, -40), 0.5)
	tween.parallel().tween_property(label, "modulate:a", 0.0, 0.5)
	tween.tween_callback(label.queue_free)
