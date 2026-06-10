extends Area2D

@export var speed: float = 250.0
@export var damage: int = 5
@export var lifetime: float = 3.0 # Akan hancur otomatis dalam 3 detik agar tidak membebani memori

var direction: Vector2 = Vector2.ZERO

func _ready():
	body_entered.connect(_on_body_entered)
	
	# Timer penghancur otomatis
	var timer = Timer.new()
	timer.wait_time = lifetime
	timer.one_shot = true
	timer.autostart = true
	timer.timeout.connect(queue_free)
	add_child(timer)

func _physics_process(delta):
	position += direction * speed * delta

func _on_body_entered(body):
	# Jika menabrak Player, berikan damage dan hancurkan peluru
	if body.is_in_group("Player") and body.has_method("take_damage"):
		body.take_damage(damage, global_position)
		queue_free()
	# Jika menabrak dinding (TileMap / StaticBody2D), peluru hancur
	elif body is TileMap or body is StaticBody2D:
		queue_free()
