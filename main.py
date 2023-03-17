@namespace
class SpriteKind:
    Helicopter = SpriteKind.create()
    CLoud = SpriteKind.create()

def on_up_pressed():
    global direction
    direction = "Up"
    FigureMan.set_image(img("""
        . . . . . . . 1 1 1 . . . . . . 
                . . . . . . . 1 1 1 . . . . . . 
                . . . . . . . 1 1 1 . . . . . . 
                . . . . . . . . 1 . . . . . . . 
                . . . . . . . 1 1 1 . . . . . . 
                . . . . . . . 1 1 1 . . . . . . 
                . . . . . . . 1 1 1 . . . . . . 
                . . . . . . . f 1 1 . . . . . . 
                . . . . . . . . 1 1 . . . . . . 
                . . . . . . . . 1 . . . . . . . 
                . . . . . . . . 1 . . . . . . . 
                . . . . . . . . 1 . . . . . . . 
                . . . . . . . 1 . 1 . . . . . . 
                . . . . . . . 1 . 1 . . . . . . 
                . . . . . . . 1 . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile(sprite, location):
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy, effects.fire, 500)
scene.on_overlap_tile(SpriteKind.enemy,
    sprites.castle.tile_dark_grass3,
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    
    def on_debounce():
        game.splash("Beware of mysterious figures.")
    timer.debounce("action", 500, on_debounce)
    
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile6
    """),
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy, effects.fire, 500)
scene.on_overlap_tile(SpriteKind.enemy,
    sprites.castle.tile_dark_grass1,
    on_overlap_tile3)

def on_a_pressed():
    
    def on_debounce2():
        global Bullet
        if direction == "Left":
            Bullet = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . 4 4 4 4 . . . . . . 
                                    . . . . . 4 5 5 5 5 4 . . . . . 
                                    . . . . . 4 5 5 5 5 4 . . . . . 
                                    . . . . . . 4 4 4 4 . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                FigureMan,
                -300,
                0)
        elif direction == "Right":
            Bullet = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . 4 4 4 4 . . . . . . 
                                    . . . . . 4 5 5 5 5 4 . . . . . 
                                    . . . . . 4 5 5 5 5 4 . . . . . 
                                    . . . . . . 4 4 4 4 . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                FigureMan,
                300,
                0)
        elif direction == "Up":
            Bullet = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . 4 4 . . . . . . . 
                                    . . . . . . 4 5 5 4 . . . . . . 
                                    . . . . . . 4 5 5 4 . . . . . . 
                                    . . . . . . 4 5 5 4 . . . . . . 
                                    . . . . . . 4 5 5 4 . . . . . . 
                                    . . . . . . . 4 4 . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                FigureMan,
                0,
                -300)
        elif direction == "Down":
            Bullet = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . 4 4 . . . . . . . 
                                    . . . . . . 4 5 5 4 . . . . . . 
                                    . . . . . . 4 5 5 4 . . . . . . 
                                    . . . . . . 4 5 5 4 . . . . . . 
                                    . . . . . . 4 5 5 4 . . . . . . 
                                    . . . . . . . 4 4 . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                FigureMan,
                0,
                300)
        Bullet.start_effect(effects.fire)
        music.play(music.melody_playable(music.knock),
            music.PlaybackMode.UNTIL_DONE)
    timer.debounce("action", 50, on_debounce2)
    
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile4(sprite4, location4):
    clearlevel()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile4
    """),
    on_overlap_tile4)

def on_left_pressed():
    global direction
    direction = "Left"
    FigureMan.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . 1 1 1 . . . . . . . 
                . . . . . . f 1 1 . . . . . . . 
                . . . . . . 1 1 1 . . . . . . . 
                . . . . . . . 1 . . . . . . . . 
                . . . . . . 1 1 1 . . . . . . . 
                . . f f f . 1 1 1 . . . . . . . 
                . . . . 1 1 1 1 1 . . . . . . . 
                . . . . f . . 1 1 . . . . . . . 
                . . . . . . . 1 1 . . . . . . . 
                . . . . . . . 1 . . . . . . . . 
                . . . . . . . 1 . . . . . . . . 
                . . . . . . 1 1 . . . . . . . . 
                . . . . . 1 . 1 . . . . . . . . 
                . . . . . 1 . . 1 1 1 . . . . . 
                . . . . . 1 . . . . . . . . . .
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile5(sprite5, location5):
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy, effects.fire, 500)
scene.on_overlap_tile(SpriteKind.enemy,
    assets.tile("""
        myTile
    """),
    on_overlap_tile5)

def on_on_overlap(sprite6, otherSprite):
    info.change_life_by(1)
    sprites.destroy(healing_thing)
sprites.on_overlap(SpriteKind.food, SpriteKind.player, on_on_overlap)

def on_right_pressed():
    global direction
    direction = "Right"
    FigureMan.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . 1 1 1 . . . . . . 
                . . . . . . . 1 1 f . . . . . . 
                . . . . . . . 1 1 1 . . . . . . 
                . . . . . . . . 1 . . . . . . . 
                . . . . . . . 1 1 1 . . . . . . 
                . . . . . . . 1 1 1 . f f f . . 
                . . . . . . . 1 1 1 1 1 . . . . 
                . . . . . . . 1 1 . . f . . . . 
                . . . . . . . 1 1 . . . . . . . 
                . . . . . . . . 1 . . . . . . . 
                . . . . . . . . 1 . . . . . . . 
                . . . . . . . . 1 1 . . . . . . 
                . . . . . . . . 1 . 1 . . . . . 
                . . . . . 1 1 1 . . 1 . . . . . 
                . . . . . . . . . . 1 . . . . .
    """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap2(sprite7, otherSprite2):
    sprites.destroy(sprite7, effects.ashes, 500)
    scene.camera_shake(6, 500)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap2)

def clearlevel():
    global level
    for value in sprites.all_of_kind(SpriteKind.enemy):
        sprites.destroy(value)
    for value2 in sprites.all_of_kind(SpriteKind.food):
        sprites.destroy(value2)
    level += 1
    CreateLevel()
def CreateLevel():
    global healing_thing
    if level == 1:
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
        tiles.place_on_random_tile(FigureMan, assets.tile("""
            myTile2
        """))
        scene.set_background_color(15)
        for index in range(4):
            healing_thing = sprites.create(img("""
                    . . . . . . . e c 7 . . . . . . 
                                    . . . . e e e c 7 7 e e . . . . 
                                    . . c e e e e c 7 e 2 2 e e . . 
                                    . c e e e e e c 6 e e 2 2 2 e . 
                                    . c e e e 2 e c c 2 4 5 4 2 e . 
                                    c e e e 2 2 2 2 2 2 4 5 5 2 2 e 
                                    c e e 2 2 2 2 2 2 2 2 4 4 2 2 e 
                                    c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                                    c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                                    c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                                    c e e 2 2 2 2 2 2 2 2 2 2 4 2 e 
                                    . e e e 2 2 2 2 2 2 2 2 2 4 e . 
                                    . 2 e e 2 2 2 2 2 2 2 2 4 2 e . 
                                    . . 2 e e 2 2 2 2 2 4 4 2 e . . 
                                    . . . 2 2 e e 4 4 4 2 e e . . . 
                                    . . . . . 2 2 e e e e . . . . .
                """),
                SpriteKind.food)
            tiles.place_on_random_tile(healing_thing, sprites.dungeon.floor_dark0)
    elif level == 2:
        tiles.set_current_tilemap(tilemap("""
            level4
        """))
        tiles.place_on_random_tile(FigureMan, sprites.dungeon.floor_mixed)
    else:
        game.game_over(True)

def on_down_pressed():
    global direction
    direction = "Down"
    FigureMan.set_image(img("""
        . . . . . . . 1 1 1 . . . . . . 
                . . . . . . . f 1 f . . . . . . 
                . . . . . . . 1 1 1 . . . . . . 
                . . . . . . . . 1 . . . . . . . 
                . . . . . . . 1 1 1 . . . . . . 
                . . . . . . . 1 1 1 . . . . . . 
                . . . . . . . 1 1 1 . . . . . . 
                . . . . . . . 1 1 f . . . . . . 
                . . . . . . . 1 1 1 . . . . . . 
                . . . . . . . . 1 f . . . . . . 
                . . . . . . . . 1 . . . . . . . 
                . . . . . . . . 1 . . . . . . . 
                . . . . . . . 1 . 1 . . . . . . 
                . . . . . . . 1 . 1 . . . . . . 
                . . . . . . . 1 . 1 . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_on_overlap3(sprite8, otherSprite3):
    sprites.destroy(otherSprite3, effects.spray, 500)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap3)

Black_Figure: Sprite = None
healing_thing: Sprite = None
Bullet: Sprite = None
direction = ""
level = 0
FigureMan: Sprite = None
FigureMan = sprites.create(img("""
        . . . . . . . 1 1 1 . . . . . . 
            . . . . . . . f 1 f . . . . . . 
            . . . . . . . 1 1 1 . . . . . . 
            . . . . . . . . 1 . . . . . . . 
            . . . . . . . 1 1 1 . . . . . . 
            . . . . . . 1 . 1 . 1 . . . . . 
            . . . . . . 1 . 1 . 1 . . . . . 
            . . . . . . 1 . 1 . f . . . . . 
            . . . . . . 1 . 1 . 1 . . . . . 
            . . . . . . . . 1 . f . . . . . 
            . . . . . . . . 1 . . . . . . . 
            . . . . . . . . 1 . . . . . . . 
            . . . . . . . 1 . 1 . . . . . . 
            . . . . . . . 1 . 1 . . . . . . 
            . . . . . . . 1 . 1 . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(FigureMan, 100, 100)
info.set_life(3)
scene.camera_follow_sprite(FigureMan)
level = 1
CreateLevel()

def on_update_interval():
    global Black_Figure
    Black_Figure = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . f f f . . . . . . . 
                    . . . . . . f 1 f . . . . . . . 
                    . . . . . . f f f . . . . . . . 
                    . . . . . . . f . . . . . . . . 
                    . . . . . . f f f . . . . . . . 
                    . . . . . f . f . f . . . . . . 
                    . . . . . f . f . f . . . . . . 
                    . . . . . f . f . f . . . . . . 
                    . . . . . . . f . . . . . . . . 
                    . . . . . . . f . . . . . . . . 
                    . . . . . . f . f . . . . . . . 
                    . . . . . . f . f . . . . . . . 
                    . . . . . . f . f . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    Black_Figure.follow(FigureMan, 30)
    Black_Figure.set_position(scene.screen_width(), randint(0, scene.screen_height()))
    Black_Figure.set_flag(SpriteFlag.AUTO_DESTROY, True)
    tiles.place_on_random_tile(Black_Figure, assets.tile("""
        myTile0
    """))
    tiles.place_on_random_tile(Black_Figure, assets.tile("""
        myTile5
    """))
game.on_update_interval(1, on_update_interval)
