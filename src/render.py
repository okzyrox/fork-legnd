from . import *

def render():
    # Clear
    renderer.clear()

    # Render map
    for tile in tiles:
        dstrect = tile.dstrect
        dstrect.x -= camera.x
        dstrect.y -= camera.y
        renderer.copy(tile.spriteSheet[tile.spriteIndex].data, dstrect = dstrect.array())

    # Render player
    for actor in actors:
        dstrect = actor.dstrect
        dstrect.x -= camera.x
        dstrect.y -= camera.y
        renderer.copy(actor.spriteSheet[actor.spriteIndex].data, dstrect = dstrect.array())

    # Flip backbuffer
    renderer.present()