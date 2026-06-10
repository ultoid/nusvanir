extends Node2D

var max_range: float = 250.0
var aoe_radius: float = 60.0

var frozen: bool = false
var global_target_pos: Vector2 = Vector2.ZERO

func _ready():
	z_index = 100 # Pastikan indikator digambar di atas segalanya
	
func _process(_delta):
	queue_redraw()

func start_casting(target_global: Vector2):
	frozen = true
	global_target_pos = target_global
	
	# Efek kedip
	var tween = create_tween()
	tween.set_loops()
	tween.tween_property(self, "modulate:a", 0.3, 0.2)
	tween.tween_property(self, "modulate:a", 1.0, 0.2)

func _draw():
	# 1. Menggambar batas maksimal cast (Lingkaran besar berpusat di player)
	draw_arc(Vector2.ZERO, max_range, 0, TAU, 64, Color(0.2, 0.8, 1.0, 0.6), 3.0)
	draw_circle(Vector2.ZERO, max_range, Color(0.2, 0.8, 1.0, 0.15))
	
	# 2. Menggambar area efek di lokasi mouse (Lingkaran merah)
	var mouse_pos = to_local(global_target_pos) if frozen else get_local_mouse_position()
	
	# Batasi indikator mouse agar tidak keluar dari jangkauan maksimal
	if not frozen and mouse_pos.length() > max_range:
		mouse_pos = mouse_pos.normalized() * max_range
	
	draw_circle(mouse_pos, aoe_radius, Color(1.0, 0.2, 0.2, 0.5))
	draw_arc(mouse_pos, aoe_radius, 0, TAU, 32, Color(1.0, 0.2, 0.2, 0.9), 2.0)
