extends CharacterBody2D

@export var speed: float = 80.0
@export var max_health: int = 30
@export var damage: int = 5

@export var chase_radius: float = 150.0
@export var lose_interest_radius: float = 250.0
var is_chasing: bool = false

var current_health: int
var player: Node2D = null
var knockback_velocity: Vector2 = Vector2.ZERO
var attack_cooldown: float = 0.0
var spawn_position: Vector2 = Vector2.ZERO

@onready var hurtbox = get_node_or_null("Hurtbox")

func _ready():
	current_health = max_health
	spawn_position = global_position # Ingat posisi lahir/awal
	# Masukkan musuh ke grup Enemy agar bisa diserang pedang
	add_to_group("Enemy")
	
	# Cari player di dalam scene
	var players = get_tree().get_nodes_in_group("Player")
	if players.size() > 0:
		player = players[0]

func _physics_process(delta):
	if attack_cooldown > 0:
		attack_cooldown -= delta
		
	# Prioritaskan gerakan pantulan (knockback) jika sedang terpental
	if knockback_velocity != Vector2.ZERO:
		velocity = knockback_velocity
		# Kurangi kecepatan pantulan seiring waktu (efek gesekan)
		knockback_velocity = knockback_velocity.move_toward(Vector2.ZERO, 600 * delta)
	else:
		# Jika tidak terpental, bergerak normal mengejar player
		if player:
			var distance = global_position.distance_to(player.global_position)
			
			# Logika Aggro (Sensor Jarak)
			if not is_chasing and distance <= chase_radius:
				is_chasing = true
			elif is_chasing and distance >= lose_interest_radius:
				is_chasing = false
				
			if is_chasing:
				if distance > 20.0:
					var direction = (player.global_position - global_position).normalized()
					velocity = direction * speed
				else:
					velocity = Vector2.ZERO
			else:
				# Jika tidak mengejar, berjalan santai pulang ke titik awal
				var dist_to_spawn = global_position.distance_to(spawn_position)
				if dist_to_spawn > 5.0:
					var return_dir = (spawn_position - global_position).normalized()
					velocity = return_dir * (speed * 0.8) # Jalan pulang sedikit lebih lambat
				else:
					velocity = Vector2.ZERO
			
	move_and_slide()
	
	# Logika Serangan Berkelanjutan
	if attack_cooldown <= 0.0 and hurtbox:
		var bodies = hurtbox.get_overlapping_bodies()
		for body in bodies:
			if body.is_in_group("Player") and body.has_method("take_damage"):
				body.take_damage(damage, global_position)
				attack_cooldown = 1.0 # Jeda 1 detik antar gigitan
				
				# Efek menerkam mundur setelah menggigit
				var bounce_dir = (global_position - body.global_position).normalized()
				knockback_velocity = bounce_dir * 120.0
				break

func take_damage(amount: int, knockback_source: Vector2 = Vector2.ZERO):
	current_health -= amount
	print("Musuh terkena serangan! HP musuh: ", current_health)
	
	spawn_damage_text(amount, Color(1, 1, 1)) # Warna Putih untuk musuh
	
	# Kalkulasi efek pantulan (Knockback)
	if knockback_source != Vector2.ZERO:
		# Cari arah menjauh dari sumber serangan
		var knockback_direction = (global_position - knockback_source).normalized()
		# Terapkan daya pantul (angka 200 bisa diubah sesuai selera)
		knockback_velocity = knockback_direction * 200.0
	
	# Efek visual sederhana (berkedip)
	modulate = Color(1, 0, 0) # Warna merah
	await get_tree().create_timer(0.1).timeout
	modulate = Color(1, 1, 1) # Normal kembali
	
	if current_health <= 0:
		if player and not player.is_dead:
			player.enemies_killed += 1
		drop_loot()
		queue_free()

func drop_loot():
	# Drop Koin (50% kesempatan)
	if randf() > 0.5:
		var coin_scene = load("res://Scenes/Items/coin.tscn")
		if coin_scene:
			var coin = coin_scene.instantiate()
			coin.global_position = global_position
			get_tree().current_scene.call_deferred("add_child", coin)
			
	# Drop EXP (Pasti drop 1 EXP)
	var exp_scene = load("res://Scenes/Items/exp_gem.tscn")
	if exp_scene:
		var exp_gem = exp_scene.instantiate()
		exp_gem.global_position = global_position
		get_tree().current_scene.call_deferred("add_child", exp_gem)

func spawn_damage_text(amount: int, color: Color):
	var label = Label.new()
	label.text = str(amount)
	label.modulate = color
	label.global_position = global_position + Vector2(-5, -20)
	label.z_index = 100 
	
	get_tree().current_scene.add_child(label)
	
	var tween = label.create_tween()
	tween.tween_property(label, "global_position", label.global_position + Vector2(0, -30), 0.6).set_ease(Tween.EASE_OUT).set_trans(Tween.TRANS_CUBIC)
	tween.parallel().tween_property(label, "modulate:a", 0.0, 0.6).set_ease(Tween.EASE_IN)
	tween.tween_callback(label.queue_free)

# Signal ini disambungkan dari Area2D (Hurtbox musuh) ketika mengenai sesuatu
func _on_hurtbox_body_entered(body):
	# Dikosongkan karena sistem serangan diganti ke _physics_process
	pass
