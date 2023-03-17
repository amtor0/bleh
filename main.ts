namespace SpriteKind {
    export const Helicopter = SpriteKind.create()
    export const CLoud = SpriteKind.create()
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    direction = "Up"
    FigureMan.setImage(img`
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
        `)
})
scene.onOverlapTile(SpriteKind.Enemy, sprites.castle.tileDarkGrass3, function (sprite, location) {
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy, effects.fire, 500)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile6`, function (sprite, location) {
    timer.debounce("action", 500, function () {
        game.splash("Beware of mysterious figures.")
    })
})
scene.onOverlapTile(SpriteKind.Enemy, sprites.castle.tileDarkGrass1, function (sprite, location) {
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy, effects.fire, 500)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    timer.debounce("action", 50, function () {
        if (direction == "Left") {
            Bullet = sprites.createProjectileFromSprite(img`
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
                `, FigureMan, -300, 0)
        } else if (direction == "Right") {
            Bullet = sprites.createProjectileFromSprite(img`
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
                `, FigureMan, 300, 0)
        } else if (direction == "Up") {
            Bullet = sprites.createProjectileFromSprite(img`
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
                `, FigureMan, 0, -300)
        } else if (direction == "Down") {
            Bullet = sprites.createProjectileFromSprite(img`
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
                `, FigureMan, 0, 300)
        }
        Bullet.startEffect(effects.fire)
        music.play(music.melodyPlayable(music.knock), music.PlaybackMode.UntilDone)
    })
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile4`, function (sprite, location) {
    clearlevel()
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    direction = "Left"
    FigureMan.setImage(img`
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
        `)
})
scene.onOverlapTile(SpriteKind.Enemy, assets.tile`myTile`, function (sprite, location) {
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy, effects.fire, 500)
})
sprites.onOverlap(SpriteKind.Food, SpriteKind.Player, function (sprite, otherSprite) {
    info.changeLifeBy(1)
    sprites.destroy(healing_thing)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    direction = "Right"
    FigureMan.setImage(img`
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
        `)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite, otherSprite) {
    sprites.destroy(sprite, effects.ashes, 500)
    scene.cameraShake(6, 500)
    info.changeLifeBy(-1)
})
function clearlevel () {
    for (let value of sprites.allOfKind(SpriteKind.Enemy)) {
        sprites.destroy(value)
    }
    for (let value of sprites.allOfKind(SpriteKind.Food)) {
        sprites.destroy(value)
    }
    level += 1
    CreateLevel()
}
function CreateLevel () {
    if (level == 1) {
        tiles.setCurrentTilemap(tilemap`level1`)
        tiles.placeOnRandomTile(FigureMan, assets.tile`myTile2`)
        scene.setBackgroundColor(15)
        for (let index = 0; index < 4; index++) {
            healing_thing = sprites.create(img`
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
                `, SpriteKind.Food)
            tiles.placeOnRandomTile(healing_thing, sprites.dungeon.floorDark0)
        }
    } else if (level == 2) {
        tiles.setCurrentTilemap(tilemap`level4`)
        tiles.placeOnRandomTile(FigureMan, sprites.dungeon.floorMixed)
    } else {
        game.gameOver(true)
    }
}
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    direction = "Down"
    FigureMan.setImage(img`
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
        `)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(otherSprite, effects.spray, 500)
    info.changeScoreBy(1)
})
let Black_Figure: Sprite = null
let healing_thing: Sprite = null
let Bullet: Sprite = null
let direction = ""
let level = 0
let FigureMan: Sprite = null
FigureMan = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(FigureMan, 100, 100)
info.setLife(3)
scene.cameraFollowSprite(FigureMan)
level = 1
CreateLevel()
game.onUpdateInterval(1, function () {
    Black_Figure = sprites.create(img`
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
        `, SpriteKind.Enemy)
    Black_Figure.follow(FigureMan, 30)
    Black_Figure.setPosition(scene.screenWidth(), randint(0, scene.screenHeight()))
    Black_Figure.setFlag(SpriteFlag.AutoDestroy, true)
    tiles.placeOnRandomTile(Black_Figure, assets.tile`myTile0`)
    tiles.placeOnRandomTile(Black_Figure, assets.tile`myTile5`)
})
