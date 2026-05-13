import sys

sys.path.insert(
    0,
    r"c:\University\Second Year Programming\2AA4\2aa4-2026-base\assignments\visualize\catanatron",
)
from catanatron.models.map import BASE_MAP_TEMPLATE, initialize_tiles, CatanMap, NodeRef

tiles = initialize_tiles(BASE_MAP_TEMPLATE)
cmap = CatanMap.from_tiles(tiles)

print("Catanatron Native Nodes for each Land Tile Coordinate:")
print("Order is always: NORTH, NORTHEAST, SOUTHEAST, SOUTH, SOUTHWEST, NORTHWEST")

# The expected java tiles order is spiral:
spiral_coords = [
    (0, 0, 0),
    (0, -1, 1),
    (-1, 0, 1),
    (-1, 1, 0),
    (0, 1, -1),
    (1, 0, -1),
    (1, -1, 0),
    (0, -2, 2),
    (-1, -1, 2),
    (-2, 0, 2),
    (-2, 1, 1),
    (-2, 2, 0),
    (-1, 2, -1),
    (0, 2, -2),
    (1, 1, -2),
    (2, 0, -2),
    (2, -1, -1),
    (2, -2, 0),
    (1, -2, 1),
]

for i, coord in enumerate(spiral_coords):
    tile = cmap.land_tiles[coord]
    order = [
        NodeRef.NORTH,
        NodeRef.NORTHEAST,
        NodeRef.SOUTHEAST,
        NodeRef.SOUTH,
        NodeRef.SOUTHWEST,
        NodeRef.NORTHWEST,
    ]
    arr = [tile.nodes[r] for r in order]
    print(f"Index {i} (Coord {coord}): {arr}")

edges = list(cmap.edges)
print("Total true edges:", len(edges))
