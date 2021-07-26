# https://www.ursinaengine.org/inventory_tutorial.html

from ursina import *
import random


class Inventory(Entity):
    def __init__(self):
        super().__init__(
            # default parent is scene, which means it's in 3d space. to use UI space, set the parent to camera.ui instead.
            parent=camera.ui,
            model='quad',
            scale=(.5, .8),
            origin=(-.5, .5),
            position=(-.3, .4),
            texture='white_cube',
            texture_scale=(5, 8),
            color=color.dark_gray
        )

        # Scaled down for each cube
        self.item_parent = Entity(parent=self, scale=(1/5, 1/8))

    def find_free_spot(self):
        taken_spots = [(int(e.x), int(e.y)) for e in self.item_parent.children]
        for y in range(8):
            for x in range(5):
                if not (x, -y) in taken_spots:
                    return (x, -y)

    def append(self, item):
        icon = Draggable(
            parent=inventory.item_parent,
            model='quad',
            texture=item,
            color=color.white,
            origin=(-.5, .5),
            position=self.find_free_spot(),
            z=-.1,
        )
        name = item.replace('_', ' ').title()
        icon.tooltip = Tooltip(name)
        icon.tooltip.background.color = color.color(0, 0, 0, .8)

        def drag():
            icon.org_pos = (icon.x, icon.y)
            icon.z -= .01   # ensure the dragged item overlaps the rest

        def drop():
            icon.x = int(icon.x)
            icon.y = int(icon.y)
            icon.z += .01

            '''if outside, return to original position'''
            if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                icon.position = (icon.org_pos)
                return

            '''if the spot is taken, swap positions'''
            for c in self.children:
                if c == icon:
                    continue

                if c.x == icon.x and c.y == icon.y:
                    print('swap positions')
                    c.position = icon.org_pos

        icon.drag = drag
        icon.drop = drop


if __name__ == "__main__":
    app = Ursina()
    inventory = Inventory()

    def add_item():
        inventory.append(random.choice(
            ('bag', 'bow_arrow', 'gem', 'orb', 'sword')))

    for i in range(7):
        add_item()

    add_item_button = Button(
        scale=(.1, .1),
        x=-.5,
        color=color.lime.tint(-.25),
        text='+',
        tooltip=Tooltip('Add random item'),
        on_click=add_item
    )
    app.run()
