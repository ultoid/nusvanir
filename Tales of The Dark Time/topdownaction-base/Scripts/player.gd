extends CharacterBody2D

signal health_changed(current_health: int, max_health: int)
signal mana_changed(current_mana: int, max_mana: int)
signal energy_changed(current_energy: float, max_energy: float)
signal player_died(survival_time: float, enemies_killed: int, level: int, coins: int)
signal coin_changed(coins: int)
signal exp_changed(current_exp: int, max_exp: int, level: int)

@export var max_health: int = 100
@export var base_attack_duration: float = 0.6 

var current_health: int
var current_mana: int
var max_mana: int = 50

var current_energy: float = 100.0
var max_energy: float = 100.0
var energy_regen: float = 7.5 # Regen 7.5 energy / sec

var knockback_velocity: Vector2 = Vector2.ZERO

# 6 Base Stats
var stat_str: int = 5
var stat_vit: int = 5
var stat_int: int = 5
var stat_luk: int = 5
var stat_agi: int = 5
var stat_dex: int = 5
var stat_points: int = 0

# Derived stats
var physical_attack: int = 10
var magic_attack: int = 10
var casting_speed: float = 1.0
var physical_defense: int = 0
var magic_defense: int = 0
var critical_chance: float = 0.0
var walk_speed: float = 100.0
var run_speed: float = 150.0
var attack_speed_multiplier: float = 1.0
var accuracy: float = 1.0

var current_attack_damage: int = 10

var coins: int = 0
var level: int = 1
var current_exp: int = 0
var max_exp: int = 10

var is_attacking: bool = false
var current_attack_speed: float = 1.0
var is_charge_attacking: bool = false
var last_direction: Vector2 = Vector2.DOWN

var is_dead: bool = false
var survival_time: float = 0.0
var enemies_killed: int = 0

var is_dashing: bool = false
var is_casting: bool = false

var is_targeting: bool = false
var current_targeting_skill: String = ""
var target_pos: Vector2 = Vector2.ZERO
var target_indicator_node: Node2D = null

var dash_timer: float = 0.0
var dash_duration: float = 0.2
var dash_speed: float = 300.0
var dash_cooldown: float = 3.0
var current_dash_cooldown: float = 0.0

var last_tap_key: String = ""
var last_tap_time: float = 0.0

var is_jumping: bool = false
var jump_timer: float = 0.0
var jump_duration: float = 0.5
var jump_height: float = 15.0
var base_y_offset: float = 0.0
var jump_cooldown: float = 0.0

var charge_attack_cooldown: float = 0.0
var charge_lunge_timer: float = 0.0

@onready var animation_tree = get_node_or_null("AnimationTree")
@onready var state_machine = animation_tree.get("parameters/playback") if animation_tree else null
@onready var sword_hitbox = get_node_or_null("SwordHitBox/CollisionShape2D")
@onready var animation_player = get_node_or_null("AnimationPlayer")
@onready var sprite = get_node_or_null("Sprite2D") # To offset jump

func get_equipment_bonuses() -> Dictionary:
	var bonuses = {
		"str": 0, "vit": 0, "int": 0, "luk": 0, "agi": 0, "dex": 0,
		"p_atk": 0, "m_atk": 0, "p_def": 0, "m_def": 0,
		"max_hp": 0, "max_mp": 0
	}
	
	if not get_node_or_null("/root/Global"): return bonuses
	var item_db = get_node_or_null("/root/ItemDB")
	if not item_db: return bonuses
	
	for slot in Global.equipment.keys():
		var item_id = Global.equipment[slot]
		if item_id != "":
			var data = item_db.get_item(item_id)
			bonuses["str"] += data.get("bonus_str", 0)
			bonuses["vit"] += data.get("bonus_vit", 0)
			bonuses["int"] += data.get("bonus_int", 0)
			bonuses["luk"] += data.get("bonus_luk", 0)
			bonuses["agi"] += data.get("bonus_agi", 0)
			bonuses["dex"] += data.get("bonus_dex", 0)
			bonuses["p_atk"] += data.get("bonus_p_atk", 0)
			bonuses["m_atk"] += data.get("bonus_m_atk", 0)
			bonuses["p_def"] += data.get("bonus_p_def", 0)
			bonuses["m_def"] += data.get("bonus_m_def", 0)
			bonuses["max_hp"] += data.get("bonus_max_hp", 0)
			bonuses["max_mp"] += data.get("bonus_max_mp", 0)
			
	return bonuses

func recalculate_stats():
	var bonuses = get_equipment_bonuses()
	var old_max_hp = max_health
	var old_max_mp = max_mana
	
	var t_str = stat_str + bonuses["str"]
	var t_vit = stat_vit + bonuses["vit"]
	var t_int = stat_int + bonuses["int"]
	var t_luk = stat_luk + bonuses["luk"]
	var t_agi = stat_agi + bonuses["agi"]
	var t_dex = stat_dex + bonuses["dex"]
	
	max_health = 50 + (t_vit * 10) + bonuses["max_hp"]
	max_mana = 20 + (t_int * 5) + bonuses["max_mp"]
	max_energy = 50.0 + (t_str * 10.0)
	
	physical_defense = t_vit + bonuses["p_def"]
	magic_defense = int(t_vit / 2.0 + t_int / 2.0) + bonuses["m_def"]
	
	if max_health > old_max_hp:
		current_health += (max_health - old_max_hp)
	if max_mana > old_max_mp:
		current_mana += (max_mana - old_max_mp)
		
	walk_speed = 80.0 + (t_agi * 4.0)
	run_speed = 120.0 + (t_agi * 6.0)
	attack_speed_multiplier = 1.0 + (t_agi * 0.05)
	energy_regen = 5.0 + (t_agi * 0.5)
	
	physical_attack = 10 + (t_str * 2) + bonuses["p_atk"]
	magic_attack = 10 + (t_int * 2) + bonuses["m_atk"]
	casting_speed = 1.0 + (t_dex * 0.05)
	critical_chance = t_luk * 1.0
	accuracy = 1.0 + (t_dex * 0.05)
	
	if get_node_or_null("/root/Global"):
		Global.perm_stat_str = stat_str
		Global.perm_stat_vit = stat_vit
		Global.perm_stat_int = stat_int
		Global.perm_stat_luk = stat_luk
		Global.perm_stat_agi = stat_agi
		Global.perm_stat_dex = stat_dex
	
	emit_signal("health_changed", current_health, max_health)

func _ready():
	if get_node_or_null("/root/Global"):
		coins = Global.coins
		level = Global.level
		current_exp = Global.current_exp
		max_exp = Global.max_exp
		stat_str = Global.perm_stat_str
		stat_vit = Global.perm_stat_vit
		stat_int = Global.perm_stat_int
		stat_luk = Global.perm_stat_luk
		stat_agi = Global.perm_stat_agi
		stat_dex = Global.perm_stat_dex
		
	recalculate_stats()
	current_health = max_health
	current_mana = max_mana
	current_energy = max_energy
	if sprite:
		base_y_offset = sprite.position.y
		
	if sword_hitbox:
		sword_hitbox.set_deferred("disabled", true)
	if animation_tree:
		animation_tree.active = true
	
	add_to_group("Player")
	
	call_deferred("emit_signal", "health_changed", current_health, max_health)
	call_deferred("emit_signal", "mana_changed", current_mana, max_mana)
	call_deferred("emit_signal", "energy_changed", current_energy, max_energy)
	call_deferred("emit_signal", "coin_changed", coins)
	call_deferred("emit_signal", "exp_changed", current_exp, max_exp, level)

func _unhandled_input(event):
	if is_targeting:
		if event is InputEventMouseButton:
			if event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
				target_pos = get_global_mouse_position()
				if current_targeting_skill != "":
					var skill_db = get_node_or_null("/root/SkillDB")
					if skill_db:
						var data = skill_db.get_skill(current_targeting_skill)
						var max_range = data.get("range", 250.0)
						if global_position.distance_to(target_pos) > max_range:
							target_pos = global_position + (target_pos - global_position).normalized() * max_range
				
				_end_targeting(true)
				get_viewport().set_input_as_handled()
			elif event.button_index == MOUSE_BUTTON_RIGHT and event.pressed:
				_end_targeting(false)
				get_viewport().set_input_as_handled()

func _end_targeting(confirm: bool):
	Engine.time_scale = 1.0
	
	var indicator = target_indicator_node
	target_indicator_node = null
	
	if confirm and current_targeting_skill != "":
		if is_instance_valid(indicator):
			indicator.start_casting(target_pos)
			
		var skill_db = get_node_or_null("/root/SkillDB")
		if skill_db:
			var data = skill_db.get_skill(current_targeting_skill)
			var cost = data.get("mp_cost", 10)
			_start_cast_skill(current_targeting_skill, data, cost, target_pos, indicator)
	else:
		if is_instance_valid(indicator):
			indicator.queue_free()

	# Tunda 1 frame agar _physics_process tidak membaca klik yang sama sebagai attack
	await get_tree().process_frame
	is_targeting = false

func _unhandled_key_input(event):
	if event.pressed and not event.echo:
		if event.physical_keycode == KEY_F1:
			print("DEBUG: Level Up +1")
			level_up()
		elif event.physical_keycode == KEY_F2:
			print("DEBUG: Koin +1000")
			add_coin(1000)

	if event.is_action_pressed("open_inventory"):
		_open_inventory()
	elif event.is_action_pressed("open_menu"):
		toggle_menu()
	elif event.is_action_pressed("open_skill_menu"):
		_open_skill_menu()
	elif event.is_action_pressed("item_1"):
		_use_quick_item(0)
	elif event.is_action_pressed("item_2"):
		_use_quick_item(1)
	elif event.is_action_pressed("skill_1"):
		_use_skill(0)
	elif event.is_action_pressed("skill_2"):
		_use_skill(1)
	elif event.is_action_pressed("skill_3"):
		_use_skill(2)
	elif event.is_action_pressed("skill_4"):
		_use_skill(3)

func _use_quick_item(slot_index: int):
	if is_dead or not get_node_or_null("/root/Global"): return
	var item_id = Global.quick_items[slot_index]
	if item_id != "" and Global.inventory.get(item_id, 0) > 0:
		var heal_amt = 50
		if get_node_or_null("/root/ItemDB"):
			var item_data = ItemDB.get_item(item_id)
			if item_data.has("effect_amount"):
				heal_amt = item_data["effect_amount"]
		
		if item_id == "potion":
			restore_hp(heal_amt)
		elif item_id == "ether":
			restore_mp(heal_amt)
			
		Global.inventory[item_id] -= 1
		
		var hud = get_tree().current_scene.get_node_or_null("PlayerHUD")
		if hud and hud.has_method("_update_quick_items"):
			hud._update_quick_items()

func _open_inventory():
	var existing = get_tree().current_scene.get_node_or_null("InventoryMenu")
	if existing:
		existing.queue_free()
		get_tree().paused = false
	else:
		var scene = load("res://Scenes/UI/inventory_menu.tscn")
		if scene and get_tree().current_scene:
			var menu = scene.instantiate()
			get_tree().current_scene.add_child(menu)
			menu.setup(self)
			get_tree().paused = true

func _open_skill_menu():
	var existing = get_tree().current_scene.get_node_or_null("SkillMenu")
	if existing:
		existing.queue_free()
		get_tree().paused = false
	else:
		var scene = load("res://Scenes/UI/skill_menu.tscn")
		if scene and get_tree().current_scene:
			var menu = scene.instantiate()
			get_tree().current_scene.add_child(menu)
			menu.setup(self)
			get_tree().paused = true

func _use_skill(slot_index: int):
	if is_dead or is_casting or is_attacking or is_dashing or is_targeting or not get_node_or_null("/root/Global"): return
	var skill_id = Global.quick_skills[slot_index]
	if skill_id == "": return
	
	var skill_db = get_node_or_null("/root/SkillDB")
	if not skill_db: return
	
	var data = skill_db.get_skill(skill_id)
	if data.is_empty(): return
	
	var cost = data.get("mp_cost", 10)
	if current_mana < cost:
		spawn_floating_text("MP Tidak Cukup!", Color(0.2, 0.5, 1))
		return
		
	var type = data.get("type", "instant")
	if type == "target_aoe":
		is_targeting = true
		current_targeting_skill = skill_id
		Engine.time_scale = 0.2
		
		var indicator_scene = load("res://Scenes/Skills/target_indicator.tscn")
		if indicator_scene:
			target_indicator_node = indicator_scene.instantiate()
			target_indicator_node.max_range = data.get("range", 250.0)
			target_indicator_node.aoe_radius = data.get("aoe_radius", 60.0)
			add_child(target_indicator_node)
	else:
		_start_cast_skill(skill_id, data, cost, Vector2.ZERO)

func _start_cast_skill(skill_id: String, data: Dictionary, cost: int, t_pos: Vector2, indicator: Node = null):
	is_casting = true
	var cast_cancelled = false
	var base_cast_time = data.get("cast_time", 3.0)
	var final_cast_time = max(0.5, base_cast_time - (stat_dex * 0.1))
	
	var max_range = data.get("range", 250.0)
	
	# Membuat Casting Bar
	var cast_bar = ProgressBar.new()
	cast_bar.min_value = 0
	cast_bar.max_value = final_cast_time
	cast_bar.value = 0
	cast_bar.show_percentage = false
	cast_bar.custom_minimum_size = Vector2(30, 4)
	cast_bar.position = Vector2(-15, 12)
	
	var sb_bg = StyleBoxFlat.new()
	sb_bg.bg_color = Color(0.2, 0.2, 0.2, 0.8)
	var sb_fg = StyleBoxFlat.new()
	sb_fg.bg_color = Color(1.0, 0.8, 0.2, 1.0)
	cast_bar.add_theme_stylebox_override("background", sb_bg)
	cast_bar.add_theme_stylebox_override("fill", sb_fg)
	add_child(cast_bar)
	
	# Visual indikator casting
	var tween = get_tree().create_tween()
	tween.set_loops()
	tween.tween_property(self, "modulate", Color(1, 1, 1, 0.5), 0.2)
	tween.tween_property(self, "modulate", Color(1, 1, 1, 1), 0.2)
	
	var timer = 0.0
	while timer < final_cast_time:
		var dt = get_process_delta_time()
		timer += dt
		if is_instance_valid(cast_bar):
			cast_bar.value = timer
			
		if not is_casting or is_dead:
			cast_cancelled = true
			break
			
		if skill_id != "heal" and global_position.distance_to(t_pos) > max_range:
			cast_cancelled = true
			is_casting = false
			spawn_floating_text("Terlalu Jauh!", Color(1, 0.5, 0))
			break
			
		await get_tree().process_frame
	
	if is_instance_valid(cast_bar):
		cast_bar.queue_free()
		
	if is_instance_valid(indicator):
		indicator.queue_free()
	
	if not is_instance_valid(tween): return
	tween.kill()
	modulate = Color(1, 1, 1)
	
	if cast_cancelled: return
	is_casting = false
	
	current_mana -= cost
	emit_signal("mana_changed", current_mana, max_mana)
	
	if skill_id == "heal":
		var heal_amt = data.get("effect_amount", 20)
		var actual_heal = min(heal_amt, max_health - current_health)
		if actual_heal < 0: actual_heal = 0
		restore_hp(heal_amt)
		spawn_floating_text("+" + str(actual_heal) + " HP", Color(0.2, 1, 0.2))
		
		var flash_tween = get_tree().create_tween()
		modulate = Color(2.0, 2.0, 2.0)
		flash_tween.tween_property(self, "modulate", Color(1.0, 1.0, 1.0), 0.3)
	elif skill_id == "fireball":
		var fb_scene = load("res://Scenes/Skills/fireball.tscn")
		if fb_scene and get_tree().current_scene:
			var fb = fb_scene.instantiate()
			fb.global_position = t_pos
			fb.damage = int(magic_attack * data.get("effect_multiplier", 1.5))
			fb.aoe_radius = data.get("aoe_radius", 60.0)
			get_tree().current_scene.add_child(fb)

func _process(delta):
	if not is_dead:
		survival_time += delta
		
		var is_holding_shift = Input.is_action_pressed("run")
		var is_running_now = false
		
		if is_holding_shift and not is_attacking and not is_dashing and not is_jumping:
			var input_dir = Vector2(
				Input.get_action_strength("move_right") - Input.get_action_strength("move_left"),
				Input.get_action_strength("move_down") - Input.get_action_strength("move_up")
			)
			if input_dir != Vector2.ZERO:
				is_running_now = true
				
		if is_running_now and current_energy > 0:
			current_energy -= 10.0 * delta # Mengurangi 10 EP per detik
			if current_energy < 0: current_energy = 0
			emit_signal("energy_changed", current_energy, max_energy)
		elif not is_holding_shift and current_energy < max_energy:
			current_energy += energy_regen * delta
			if current_energy > max_energy: current_energy = max_energy
			emit_signal("energy_changed", current_energy, max_energy)

func _physics_process(delta):
	if is_dead: return
	
	if current_dash_cooldown > 0: current_dash_cooldown -= delta
	if charge_attack_cooldown > 0: charge_attack_cooldown -= delta
	if jump_cooldown > 0: jump_cooldown -= delta
	

	# Double tap dash
	var move_keys = ["move_up", "move_down", "move_left", "move_right"]
	for key in move_keys:
		if Input.is_action_just_pressed(key):
			var current_time = Time.get_ticks_msec() / 1000.0
			if last_tap_key == key and current_time - last_tap_time < 0.3:
				if not is_dashing and not is_attacking:
					if current_dash_cooldown <= 0:
						if current_energy >= 20.0:
							current_energy -= 20.0
							emit_signal("energy_changed", current_energy, max_energy)
							is_dashing = true
							dash_timer = dash_duration
							current_dash_cooldown = dash_cooldown
							var dir = Vector2.ZERO
							if key == "move_up": dir.y = -1
							elif key == "move_down": dir.y = 1
							elif key == "move_left": dir.x = -1
							elif key == "move_right": dir.x = 1
							last_direction = dir
							velocity = dir * dash_speed
							last_tap_key = ""
							break
						else:
							spawn_floating_text("EP Tidak Cukup!", Color(1, 0.5, 0))
							last_tap_key = ""
							break
					else:
						spawn_floating_text("Masih Cooldown!", Color(0.4, 0.6, 1))
						last_tap_key = ""
						break
			else:
				last_tap_key = key
				last_tap_time = current_time
		
	if is_dashing:
		velocity = last_direction * dash_speed
		dash_timer -= delta
		move_and_slide()
		modulate.a = 0.5
		if dash_timer <= 0:
			is_dashing = false
			modulate.a = 1.0
		return
		
	if is_jumping:
		jump_timer -= delta
		if sprite:
			var progress = 1.0 - (jump_timer / jump_duration)
			sprite.position.y = base_y_offset - sin(progress * PI) * jump_height
			
		move_and_slide() # Still sliding based on velocity
		
		if jump_timer <= 0:
			is_jumping = false
			if sprite: sprite.position.y = base_y_offset
		return

	if knockback_velocity != Vector2.ZERO:
		velocity = knockback_velocity
		knockback_velocity = knockback_velocity.move_toward(Vector2.ZERO, 800 * delta)
		move_and_slide()
		return
		
	var input_direction = Vector2(
		Input.get_action_strength("move_right") - Input.get_action_strength("move_left"),
		Input.get_action_strength("move_down") - Input.get_action_strength("move_up")
	).normalized()

	if is_attacking:
		if animation_tree and current_attack_speed != 1.0:
			animation_tree.advance(delta * (current_attack_speed - 1.0))
		
		if is_charge_attacking and charge_lunge_timer > 0:
			charge_lunge_timer -= delta
			velocity = last_direction * dash_speed
		else:
			var move_speed = walk_speed
			if Input.is_action_pressed("run") and current_energy > 0:
				move_speed = run_speed
			velocity = input_direction * move_speed
			
		move_and_slide()
		return
	
	var current_speed = walk_speed
	var anim_speed = 1.0
	
	if is_casting:
		current_speed = walk_speed * 0.5
	elif Input.is_action_pressed("run") and current_energy > 0:
		current_speed = run_speed
		if input_direction != Vector2.ZERO and not is_attacking:
			anim_speed = 2.0
			
	if animation_tree and anim_speed > 1.0:
		animation_tree.advance(delta * (anim_speed - 1.0))
		
	if input_direction != Vector2.ZERO:
		var anim_direction = input_direction
		if anim_direction.x != 0 and anim_direction.y != 0:
			anim_direction.y = 0 
		last_direction = anim_direction.normalized()
		velocity = input_direction * current_speed
		
		if animation_tree:
			animation_tree.set("parameters/Idle/blend_position", last_direction)
			animation_tree.set("parameters/Walk/blend_position", last_direction)
			animation_tree.set("parameters/Attack/blend_position", last_direction)
			if state_machine and not is_attacking:
				state_machine.travel("Walk")
	else:
		velocity = Vector2.ZERO
		if state_machine and not is_attacking:
			state_machine.travel("Idle")
		
	move_and_slide()
	
	if Input.is_action_just_pressed("basic_attack") and not is_attacking and not is_jumping and not is_casting and not is_targeting:
		attack(false)
		
	if Input.is_action_just_pressed("charge_attack") and not is_attacking and not is_jumping and not is_casting and not is_targeting:
		if charge_attack_cooldown <= 0:
			if current_energy >= 30:
				current_energy -= 30
				charge_attack_cooldown = 2.0
				emit_signal("energy_changed", current_energy, max_energy)
				attack(true)
			else:
				spawn_floating_text("EP Tidak Cukup!", Color(1, 0.5, 0))
		else:
			spawn_floating_text("Masih Cooldown!", Color(0.4, 0.6, 1))
		
	if Input.is_action_just_pressed("jump") and not is_jumping and not is_attacking and jump_cooldown <= 0:
		is_jumping = true
		jump_timer = jump_duration
		jump_cooldown = 1.0
		# Preserve velocity for the jump
		if input_direction != Vector2.ZERO:
			velocity = input_direction * current_speed

func toggle_menu():
	var existing_menu = get_tree().current_scene.get_node_or_null("CharacterMenu")
	if existing_menu:
		existing_menu.queue_free()
		get_tree().paused = false
	else:
		var char_scene = load("res://Scenes/UI/character_menu.tscn")
		if char_scene and get_tree().current_scene:
			var menu = char_scene.instantiate()
			get_tree().current_scene.add_child(menu)
			menu.setup(self)
			get_tree().paused = true

func attack(is_charge: bool):
	is_attacking = true
	is_charge_attacking = is_charge
	
	# Hitung damage dan critical chance
	var is_crit = randf() * 100.0 < critical_chance
	current_attack_damage = physical_attack
	if is_charge:
		current_attack_damage = physical_attack * 2
	if is_crit:
		current_attack_damage = int(current_attack_damage * 2.0)
		print("CRITICAL HIT!")
	
	if sword_hitbox:
		sword_hitbox.set_deferred("disabled", false)
		var area = sword_hitbox.get_parent()
		if area and area.has_method("clear_hit_list"):
			area.clear_hit_list()
	
	current_attack_speed = attack_speed_multiplier
	if is_charge: current_attack_speed *= 0.5 # Charge attack 50% lebih lambat
	
	if animation_tree:
		animation_tree.set("parameters/AttackTimeScale/scale", current_attack_speed)
	
	if state_machine:
		state_machine.travel("Attack")
		
	var current_attack_duration = base_attack_duration / current_attack_speed
	
	if is_charge:
		charge_lunge_timer = current_attack_duration * 0.2
		
	await get_tree().create_timer(current_attack_duration).timeout
	
	if is_attacking:
		attack_finished()

func attack_finished():
	is_attacking = false
	current_attack_speed = 1.0
	if sword_hitbox: sword_hitbox.set_deferred("disabled", true)
	if state_machine: state_machine.travel("Idle")

func take_damage(amount: int, knockback_source: Vector2 = Vector2.ZERO):
	if is_dead or is_dashing: return
	
	if is_casting:
		is_casting = false
		spawn_floating_text("Batal!", Color(1, 0.5, 0))
		
	var final_damage = amount - physical_defense
	if final_damage < 1: final_damage = 1
		
	current_health -= final_damage
	emit_signal("health_changed", current_health, max_health)
	spawn_damage_text(final_damage, Color(1, 0.2, 0.2))
	
	if knockback_source != Vector2.ZERO:
		var knockback_direction = (global_position - knockback_source).normalized()
		# Knockback base 250, semakin tinggi VIT, semakin lemah (minimal 50)
		var knockback_strength = max(50.0, 250.0 - (stat_vit * 10.0))
		knockback_velocity = knockback_direction * knockback_strength
		
	modulate = Color(1, 0, 0)
	await get_tree().create_timer(0.1).timeout
	modulate = Color(1, 1, 1)
	
	if current_health <= 0: die()

func spawn_damage_text(amount: int, color: Color):
	var label = Label.new()
	label.text = str(amount)
	label.modulate = color
	label.global_position = global_position + Vector2(-5, -20)
	label.z_index = 100 
	get_tree().current_scene.add_child(label)
	var tween = get_tree().create_tween()
	tween.tween_property(label, "global_position", label.global_position + Vector2(0, -30), 0.6).set_ease(Tween.EASE_OUT).set_trans(Tween.TRANS_CUBIC)
	tween.parallel().tween_property(label, "modulate:a", 0.0, 0.6).set_ease(Tween.EASE_IN)
	tween.tween_callback(label.queue_free)

func spawn_floating_text(msg: String, color: Color):
	var label = Label.new()
	label.text = msg
	label.modulate = color
	label.global_position = global_position + Vector2(-30, -40)
	label.z_index = 100 
	get_tree().current_scene.add_child(label)
	var tween = get_tree().create_tween()
	tween.tween_property(label, "global_position", label.global_position + Vector2(0, -30), 0.8).set_ease(Tween.EASE_OUT).set_trans(Tween.TRANS_CUBIC)
	tween.parallel().tween_property(label, "modulate:a", 0.0, 0.8).set_ease(Tween.EASE_IN)
	tween.tween_callback(label.queue_free)

func die():
	if is_dead: return
	is_dead = true
	if sword_hitbox: sword_hitbox.set_deferred("disabled", true)
	if animation_tree: animation_tree.active = false
	if animation_player:
		animation_player.play("Death")
		await animation_player.animation_finished
	emit_signal("player_died", survival_time, enemies_killed, level, coins)
	
	var go_scene = load("res://Scenes/UI/game_over_hud.tscn")
	if go_scene and get_tree().current_scene:
		var go = go_scene.instantiate()
		get_tree().current_scene.add_child(go)
		if go.has_method("show_game_over"):
			go.show_game_over(survival_time, enemies_killed, level, coins)

func add_coin(amount: int):
	coins += amount
	if get_node_or_null("/root/Global"): Global.coins = coins
	emit_signal("coin_changed", coins)

func add_exp(amount: int):
	current_exp += amount
	if get_node_or_null("/root/Global"): Global.current_exp = current_exp
	emit_signal("exp_changed", current_exp, max_exp, level)
	
	while current_exp >= max_exp:
		level_up()
		toggle_menu()

func restore_hp(amount: int):
	if is_dead: return
	current_health += amount
	if current_health > max_health: current_health = max_health
	emit_signal("health_changed", current_health, max_health)

func restore_mp(amount: int):
	if is_dead: return
	current_mana += amount
	if current_mana > max_mana: current_mana = max_mana
	emit_signal("mana_changed", current_mana, max_mana)

func level_up():
	level += 1
	current_exp -= max_exp
	max_exp = int(max_exp * 1.5)
	stat_points += 1
	
	if get_node_or_null("/root/Global"):
		Global.level = level
		Global.current_exp = current_exp
		Global.max_exp = max_exp
		
	emit_signal("exp_changed", current_exp, max_exp, level)
