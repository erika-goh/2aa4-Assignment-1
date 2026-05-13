import sys

sys.path.insert(
    0,
    r"c:\University\Second Year Programming\2AA4\2aa4-2026-base\assignments\visualize\catanatron",
)
from catanatron.models.map import BASE_MAP_TEMPLATE, initialize_tiles, CatanMap

tiles = initialize_tiles(BASE_MAP_TEMPLATE)
cmap = CatanMap.from_tiles(tiles)

coords = [
    (0, 0, 0),  # 0
    (0, -1, 1),  # 1
    (-1, 0, 1),  # 2
    (-1, 1, 0),  # 3
    (0, 1, -1),  # 4
    (1, 0, -1),  # 5
    (1, -1, 0),  # 6
]

for i, c in enumerate(coords):
    print(f"Tile {i} Coord {c}")

# Let's see what catanatron considers to be the neighbors of (-1, 1, 0)
print(f"Neighbors of Tile 3 (-1, 1, 0):")
t3 = cmap.land_tiles[(-1, 1, 0)]
for d, nb in t3.neighbors.items():
    print(f"  Dir {d} -> Tile {nb.coordinate if nb else 'None'}")
