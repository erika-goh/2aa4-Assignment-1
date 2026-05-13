import sys
import os

sys.path.insert(
    0,
    r"c:\University\Second Year Programming\2AA4\2aa4-2026-base\assignments\visualize\catanatron",
)
from catanatron.gym.envs.pygame_renderer import PygameRenderer

renderer = PygameRenderer()

# Test Center and Tile 3
c_center = renderer.cube_to_pixel((0, 0, 0))
c_t3 = renderer.cube_to_pixel((-1, 1, 0))
c_t1 = renderer.cube_to_pixel((0, -1, 1))

print(f"Center (0,0,0) pixel: {c_center}")
print(f"Tile 3 (-1,1,0) pixel: {c_t3}")
print(f"Tile 1 (0,-1,1) pixel: {c_t1}")

for direction in ["NORTH", "NORTHEAST", "SOUTHEAST", "SOUTH", "SOUTHWEST", "NORTHWEST"]:
    print(
        f"Delta for {direction}: {renderer.get_node_delta(direction, renderer.hex_size)}"
    )


for node_id in [15, 16]:
    # find node pixel coords
    pos = renderer.get_node_pos(node_id, game.map)
    print(f"Node {node_id} screen pos: {pos}")
