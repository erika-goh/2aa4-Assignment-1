import sys
import math

sys.path.insert(
    0,
    r"c:\University\Second Year Programming\2AA4\2aa4-2026-base\assignments\visualize\catanatron",
)
from catanatron.gym.envs.pygame_renderer import PygameRenderer
from catanatron.models.map import initialize_tiles, BASE_MAP_TEMPLATE, CatanMap
from catanatron.game import Game
from catanatron.models.player import Player, Color

tiles = initialize_tiles(BASE_MAP_TEMPLATE)
cmap = CatanMap.from_tiles(tiles)
game = Game([Player(Color.RED), Player(Color.BLUE)], catan_map=cmap)

renderer = PygameRenderer()
nodes_pos = {}
# Expose the positions from pygame!
# The draw_nodes logic in PygameRenderer computes the exact (x, y) pixels.
import pygame  # type: ignore


def get_native_pos(node_id):
    # Reverse engineer PygameRenderer's position
    # It draws circles over the board
    # find adjacent tile
    tiles = cmap.adjacent_tiles[node_id]
    tile = tiles[0]
    coord = next(k for k, v in cmap.land_tiles.items() if v == tile)

    # from PygameRenderer
    center_x, center_y = 500, 400
    q, s, r = coord
    RADIUS = 60
    HEIGHT = 2 * RADIUS
    WIDTH = math.sqrt(3) * RADIUS

    x = center_x + (WIDTH * (q + r / 2.0))
    y = center_y + (HEIGHT * (3.0 / 4.0) * r)

    # find the noderef
    noderef = next(k for k, v in tile.nodes.items() if v == node_id)

    dx, dy = 0, 0
    from catanatron.models.enums import NodeRef

    if noderef == NodeRef.NORTH:
        dy = -HEIGHT / 2
    elif noderef == NodeRef.SOUTH:
        dy = HEIGHT / 2
    elif noderef == NodeRef.NORTHEAST:
        dx = WIDTH / 2
        dy = -HEIGHT / 4
    elif noderef == NodeRef.SOUTHEAST:
        dx = WIDTH / 2
        dy = HEIGHT / 4
    elif noderef == NodeRef.NORTHWEST:
        dx = -WIDTH / 2
        dy = -HEIGHT / 4
    elif noderef == NodeRef.SOUTHWEST:
        dx = -WIDTH / 2
        dy = HEIGHT / 4

    return (x + dx, y + dy)


pos_18 = get_native_pos(18)
pos_15 = get_native_pos(15)
pos_14 = get_native_pos(14)

print(f"Native 18 pixel pos: {pos_18}")
print(f"Native 15 pixel pos: {pos_15}")
print(f"Native 14 pixel pos: {pos_14}")

# Now what is the Left Hex center?
q, s, r = (-1, 1, 0)
left_x = 500 + (math.sqrt(3) * 60 * (-1))
left_y = 400
print(f"Left Hex pixel pos: ({left_x}, {left_y})")
print(f"Top-Left of Left Hex should be: ({left_x - math.sqrt(3)*30}, {left_y - 30})")

# Top-Left Hex center?
tl_q, tl_s, tl_r = (-1, 0, 1)
tl_x = 500 + (math.sqrt(3) * 60 * (-1 + 1 / 2.0))
tl_y = 400 + (120 * 0.75 * 1)
print(f"Top-Left Hex pixel pos: ({tl_x}, {tl_y})")
print(f"Top-Left of Top-Left Hex should be: ({tl_x - math.sqrt(3)*30}, {tl_y - 30})")
