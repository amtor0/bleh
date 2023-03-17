@namespace
class SpriteKind:
    Helicopter = SpriteKind.create()
    CLoud = SpriteKind.create()

def on_up_pressed():
    animation.run_image_animation(Indian_boy,
        [img("""
                . . . . f f f f . . . . . 
                        . . f f c c c c f f . . . 
                        . f f c c c c c c f f . . 
                        f f c c c c c c c c f f . 
                        f f c c f c c c c c c f . 
                        f f f f f c c c f c c f . 
                        f f f f c c c f c c f f . 
                        f f f f f f f f f f f f . 
                        f f f f f f f f f f f f . 
                        . f f f f f f f f f f . . 
                        . f f f f f f f f f f . . 
                        f e f f f f f f f f e f . 
                        e 4 f 7 7 7 7 7 7 c 4 e . 
                        e e f 6 6 6 6 6 6 f e e . 
                        . . . f f f f f f . . . . 
                        . . . f f . . f f . . . .
            """),
            img("""
                . . . . . . . . . . . . . 
                        . . . . . f f f f . . . . 
                        . . . f f c c c c f f . . 
                        . f f f c c c c c c f f . 
                        f f c c c c c c c c c f f 
                        f c c c c f c c c c c c f 
                        . f f f f c c c c f c c f 
                        . f f f f c c f c c c f f 
                        . f f f f f f f f f f f f 
                        . f f f f f f f f f f f f 
                        . . f f f f f f f f f f . 
                        . . e f f f f f f f f f . 
                        . . e f f f f f f f f e f 
                        . . 4 c 7 7 7 7 7 e 4 4 e 
                        . . e f f f f f f f e e . 
                        . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . 
                        . . . . . f f f f . . . . 
                        . . . f f c c c c f f . . 
                        . . f f c c c c c c f f . 
                        . f f f c c c c c c c f f 
                        f f f c c c c c c c c c f 
                        f f c c c f c c c c c c f 
                        . f f f f f c c c f c f f 
                        . f f f f c c f f c f f f 
                        . . f f f f f f f f f f f 
                        . . f f f f f f f f f f . 
                        . . f f f f f f f f f e . 
                        . f e f f f f f f f f e . 
                        . e 4 4 e 7 7 7 7 7 c 4 . 
                        . . e e f f f f f f f e . 
                        . . . . . . . . f f f . .
            """)],
        100,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_a_pressed():
    if 0 == 0:
        pass
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    animation.run_image_animation(Indian_boy,
        [img("""
                . . . . . f f f f f . . . 
                        . . . f f f f f f f f f . 
                        . . f f f c f f f f f f . 
                        . . f f c f f f c f f f f 
                        f f c c f f f c c f f c f 
                        f f f f f e f f f f c c f 
                        . f f f e e f f f f f f f 
                        . . f f e e f b f e e f f 
                        . . . f 4 4 f 1 e 4 e f . 
                        . . . f 4 4 4 4 e f f f . 
                        . . . f f e e e e e f . . 
                        . . . f 7 7 7 e 4 4 e . . 
                        . . . f 7 7 7 e 4 4 e . . 
                        . . . f 6 6 6 f e e f . . 
                        . . . . f f f f f f . . . 
                        . . . . . . f f f . . . .
            """),
            img("""
                . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . 
                        . . . f f f f f f f f f . 
                        . . f f f c f f f f f f . 
                        . f f f c f f f c f f f f 
                        f f c c f f f c c f f c f 
                        f f f f f e f f f f c c f 
                        . f f f e e f f f f f f f 
                        . . f f e e f b f e e f f 
                        . . f f 4 4 f 1 e 4 e f . 
                        . . . f 4 4 4 e e f f f . 
                        . . . f f e e 4 4 e f . . 
                        . . . f 7 7 e 4 4 e f . . 
                        . . f f 6 6 f e e f f f . 
                        . . f f f f f f f f f f . 
                        . . . f f f . . . f f . .
            """),
            img("""
                . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . 
                        . . . f f f f f f f f f . 
                        . . f f f c f f f f f f . 
                        . f f f c f f f c f f f f 
                        f f c c f f f c c f f c f 
                        f f f f f e f f f f c c f 
                        . f f f e e f f f f f f f 
                        . f f f e e f b f e e f f 
                        . . f f 4 4 f 1 e 4 e f f 
                        . . . f 4 4 4 4 e f f f . 
                        . . . f f e e e e 4 4 4 . 
                        . . . f 7 7 7 7 e 4 4 e . 
                        . . f f 6 6 6 6 f e e f . 
                        . . f f f f f f f f f f . 
                        . . . f f f . . . f f . .
            """)],
        100,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    animation.run_image_animation(Indian_boy,
        [img("""
                . . . . . . . . . . . . . 
                        . . . f f f f f f . . . . 
                        . f f f f f f f f f . . . 
                        . f f f f f f c f f f . . 
                        f f f f c f f f c f f f . 
                        f c f f c c f f f c c f f 
                        f c c f f f f e f f f f f 
                        f f f f f f f e e f f f . 
                        f f e e f b f e e f f f . 
                        f f e 4 e 1 f 4 4 f f . . 
                        . f f f e 4 4 4 4 f . . . 
                        . 4 4 4 e e e e f f . . . 
                        . e 4 4 e 7 7 7 7 f . . . 
                        . f e e f 6 6 6 6 f f . . 
                        . f f f f f f f f f f . . 
                        . . f f . . . f f f . . .
            """),
            img("""
                . . . . . . . . . . . . . 
                        . . . f f f f f f . . . . 
                        . f f f f f f f f f . . . 
                        . f f f f f f c f f f . . 
                        f f f f c f f f c f f f . 
                        f c f f c c f f f c c f f 
                        f c c f f f f e f f f f f 
                        f f f f f f f e e f f f . 
                        f f e e f b f e e f f . . 
                        . f e 4 e 1 f 4 4 f f . . 
                        . f f f e e 4 4 4 f . . . 
                        . . f e 4 4 e e f f . . . 
                        . . f e 4 4 e 7 7 f . . . 
                        . f f f e e f 6 6 f f . . 
                        . f f f f f f f f f f . . 
                        . . f f . . . f f f . . .
            """),
            img("""
                . . . f f f f f . . . . . 
                        . f f f f f f f f f . . . 
                        . f f f f f f c f f f . . 
                        f f f f c f f f c f f . . 
                        f c f f c c f f f c c f f 
                        f c c f f f f e f f f f f 
                        f f f f f f f e e f f f . 
                        f f e e f b f e e f f . . 
                        . f e 4 e 1 f 4 4 f . . . 
                        . f f f e 4 4 4 4 f . . . 
                        . . f e e e e e f f . . . 
                        . . e 4 4 e 7 7 7 f . . . 
                        . . e 4 4 e 7 7 7 f . . . 
                        . . f e e f 6 6 6 f . . . 
                        . . . f f f f f f . . . . 
                        . . . . f f f . . . . . .
            """)],
        100,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    animation.run_image_animation(Indian_boy,
        [img("""
                . . . . f f f f . . . . . 
                        . . f f f f f f f f . . . 
                        . f f f f f f c f f f . . 
                        f f f f f f c c f f f c . 
                        f f f c f f f f f f f c . 
                        c c c f f f e e f f c c . 
                        f f f f f e e f f c c f . 
                        f f f b f e e f b f f f . 
                        . f 4 1 f 4 4 f 1 4 f . . 
                        . f e 4 4 4 4 4 4 e f . . 
                        . f f f e e e e f f f . . 
                        f e f b 7 7 7 7 b f e f . 
                        e 4 f 7 7 7 7 7 7 f 4 e . 
                        e e f 6 6 6 6 6 6 f e e . 
                        . . . f f f f f f . . . . 
                        . . . f f . . f f . . . .
            """),
            img("""
                . . . . . . . . . . . . . 
                        . . . . . f f f f . . . . 
                        . . . f f f f f f f f . . 
                        . . f f f f f f c f f f . 
                        f f f f f f f c c f f f c 
                        f f f f c f f f f f f f c 
                        . c c c f f f e e f f c c 
                        . f f f f f e e f f c c f 
                        . f f f b f e e f b f f f 
                        . f f 4 1 f 4 4 f 1 4 f f 
                        . . f e 4 4 4 4 4 e e f e 
                        . f e f b 7 7 7 e 4 4 4 e 
                        . e 4 f 7 7 7 7 e 4 4 e . 
                        . . . f 6 6 6 6 6 e e . . 
                        . . . f f f f f f f . . . 
                        . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . 
                        . . . . f f f f . . . . . 
                        . . f f f f f f f f . . . 
                        . f f f c f f f f f f . . 
                        c f f f c c f f f f f f f 
                        c f f f f f f f c f f f f 
                        c c f f e e f f f c c c . 
                        f c c f f e e f f f f f . 
                        f f f b f e e f b f f f . 
                        f f 4 1 f 4 4 f 1 4 f f . 
                        e f e e 4 4 4 4 4 e f . . 
                        e 4 4 4 e 7 7 7 b f e f . 
                        . e 4 4 e 7 7 7 7 f 4 e . 
                        . . e e 6 6 6 6 6 f . . . 
                        . . . f f f f f f f . . . 
                        . . . . . . . f f f . . .
            """)],
        100,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

Indian_boy: Sprite = None
Indian_boy = sprites.create(img("""
        . . . . f f f f . . . . . 
            . . f f f f f f f f . . . 
            . f f f f f f c f f f . . 
            f f f f f f c c f f f c . 
            f f f c f f f f f f f c . 
            c c c f f f e e f f c c . 
            f f f f f e e f f c c f . 
            f f f b f e e f b f f f . 
            . f 4 1 f 4 4 f 1 4 f . . 
            . f e 4 4 4 4 4 4 e f . . 
            . f f f e e e e f f f . . 
            f e f b 7 7 7 7 b f e f . 
            e 4 f 7 7 7 7 7 7 f 4 e . 
            e e f 6 6 6 6 6 6 f e e . 
            . . . f f f f f f . . . . 
            . . . f f . . f f . . . .
    """),
    SpriteKind.player)
scene.camera_follow_sprite(Indian_boy)
controller.move_sprite(Indian_boy, 100, 100)
scary_monster = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . 5 . . . . . . . 
            . . . . . . . 5 . . . . . . . . 
            . . . . . 5 5 5 5 5 . . . . . . 
            . . . . 5 5 5 5 5 5 5 . . . . . 
            . . . . 5 f 1 5 1 f 5 . . . . . 
            . . . . 5 5 5 5 5 5 5 . . . . . 
            . . . . 5 4 4 4 4 4 5 . . . . . 
            . . . . 5 5 4 4 4 5 5 . . . . . 
            . . . . . 5 5 5 5 5 . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
scary_monster.set_position(10, 105)
scary_monster.follow(Indian_boy, 30)