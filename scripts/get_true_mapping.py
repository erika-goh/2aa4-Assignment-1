import sys
import json

sys.path.insert(
    0,
    r"c:\University\Second Year Programming\2AA4\2aa4-2026-base\assignments\visualize",
)
sys.path.insert(
    0,
    r"c:\University\Second Year Programming\2AA4\2aa4-2026-base\assignments\visualize\catanatron",
)
from light_visualizer import CatanBoardVisualizer
from catanatron.models.map import NodeRef

vis = CatanBoardVisualizer()
# Create a mock base_map.json string or load it
vis.load_map_json(
    r"c:\University\Second Year Programming\2AA4\2aa4-2026-base\assignments\visualize\base_map.json"
)
cmap = vis._create_map_from_json()

coords = [
    (0, 0, 0),  # 0
    (0, -1, 1),  # 1
    (-1, 0, 1),  # 2
    (-1, 1, 0),  # 3
    (0, 1, -1),  # 4
    (1, 0, -1),  # 5
    (1, -1, 0),  # 6
    (0, -2, 2),  # 7
    (-1, -1, 2),  # 8
    (-2, 0, 2),  # 9
    (-2, 1, 1),  # 10
    (-2, 2, 0),  # 11
    (-1, 2, -1),  # 12
    (0, 2, -2),  # 13
    (1, 1, -2),  # 14
    (2, 0, -2),  # 15
    (2, -1, -1),  # 16
    (2, -2, 0),  # 17
    (1, -2, 1),  # 18
]
dir_map = [
    NodeRef.NORTH,
    NodeRef.NORTHEAST,
    NodeRef.SOUTHEAST,
    NodeRef.SOUTH,
    NodeRef.SOUTHWEST,
    NodeRef.NORTHWEST,
]

print("TRUE MAPPING ARRAY FOR JAVA:")
print("int[][] mapping = {")
for i, coord in enumerate(coords):
    tile = cmap.land_tiles[coord]
    nodes = [tile.nodes[d] for d in dir_map]
    print(
        f"    {{{nodes[0]}, {nodes[1]}, {nodes[2]}, {nodes[3]}, {nodes[4]}, {nodes[5]}}}, // Tile {i}"
    )
print("};")
