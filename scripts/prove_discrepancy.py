import sys

sys.path.insert(
    0,
    r"c:\University\Second Year Programming\2AA4\2aa4-2026-base\assignments\visualize\catanatron",
)
from catanatron.models.map import BASE_MAP_TEMPLATE, initialize_tiles, CatanMap, NodeRef

coords = [
    (0, 0, 0),  # 0 Center
    (0, -1, 1),  # 1 BR
    (-1, 0, 1),  # 2 BL
    (-1, 1, 0),  # 3 L
    (0, 1, -1),  # 4 TL
    (1, 0, -1),  # 5 TR
    (1, -1, 0),  # 6 R
]

tiles = initialize_tiles(BASE_MAP_TEMPLATE)
cmap = CatanMap.from_tiles(tiles)
tile_map = {coord: tile for coord, tile in cmap.land_tiles.items()}

# Corner order: Top, TR, BR, B, BL, TL
dir_map = [
    NodeRef.NORTH,
    NodeRef.NORTHEAST,
    NodeRef.SOUTHEAST,
    NodeRef.SOUTH,
    NodeRef.SOUTHWEST,
    NodeRef.NORTHWEST,
]

print("Catanatron Native Node IDs (Local Corners: Top, TR, BR, Bottom, BL, TL):")
for i in [0, 3]:
    cat_tile = tile_map[coords[i]]
    nodes = []
    for j in range(6):
        nodes.append(cat_tile.nodes[dir_map[j]])
    print(f"Tile {i}: {nodes}")
