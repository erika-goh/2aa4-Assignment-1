import sys

sys.path.insert(
    0,
    r"c:\University\Second Year Programming\2AA4\2aa4-2026-base\assignments\visualize\catanatron",
)
from catanatron.models.map import BASE_MAP_TEMPLATE, initialize_tiles, CatanMap, NodeRef

tiles = initialize_tiles(BASE_MAP_TEMPLATE)
cmap = CatanMap.from_tiles(tiles)

print("Catanatron Native Node Coordinates:")
for coord, tile in cmap.land_tiles.items():
    for d, n_id in tile.nodes.items():
        if n_id in [13, 14, 15]:
            print(f"Node {n_id} is at direction {d} of Tile {coord}")
