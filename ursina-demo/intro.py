# https://www.ursinaengine.org/introduction_tutorial.html

from ursina import *

app = Ursina()

# lots of preloaded models like "cube", "sphere", "quad"
# see models: https://www.ursinaengine.org/cheat_sheet.html#models
player = Entity(model="cube", color=color.orange, scale_y=2)


def update():
    """automatically called by the engine every frame"""
    player.x += held_keys['d'] * time.dt - held_keys['a'] * time.dt
    # player.y += held_keys['w'] * time.dt - held_keys['s'] * time.dt


def input(key):
    """event fired on key press"""
    if key == 'space':
        player.y += 1
        invoke(setattr, player, 'y', player.y-1, delay=.25)


app.run()
