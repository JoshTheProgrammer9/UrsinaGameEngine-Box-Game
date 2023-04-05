"""
    Name: Joshua Ludolf
    Date: 04/04/2023
    Purpose: Expermentation with Ursina Library/Building 3D Game (Get to the other side style)
"""

import ursina
from ursina import *
import random


app = Ursina()

window.title = 'My Game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = True               # Do not go Fullscreen
window.exit_button.visible = True      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True 

player = Entity(model = "cube", color = color.green, texture = "white_cube", scale = 1)
enemy = Entity(model = "cube", color = color.red, texture = "white_cube", scale = 1)

player.collider = BoxCollider(player, center=Vec3(0,0,0), size=Vec3(0.5,0.5,0.5))
enemy.collider = BoxCollider(enemy, center=Vec3(0,0,0), size=Vec3(0.5,0.5,0.5))

enemy.y = 0
enemy.x = random.randint(1,5)


def update():
    player.x += held_keys["d"] * 0.1
    player.x -= held_keys["a"] * 0.1
    player.y += held_keys["w"] * 0.1
    player.y -= held_keys["s"] * 0.1
    player.rotation_x += held_keys["r"] * 5
    player.rotation_y += held_keys["r"] * 5
    player.rotation_x -= held_keys["q"] * 5
    player.rotation_y -= held_keys["q"] * 5

    if player.intersects(enemy).hit:
        Text.size = 0.05
        Text.default_resolution = 1080 * Text.size
        info = Text(text="GAME OVER!!!")
        info.x = -0.5
        info.y = 0.4
        info.background = False
        info.visible = True

        player.disable()
        enemy.disable()
        
        
        

        
        
        
        
    else:
        enemy.y += random.randint(-2,2)
        enemy.rotation_x += 2.5
        enemy.rotation_y += 2.5
        
        



app.run()

