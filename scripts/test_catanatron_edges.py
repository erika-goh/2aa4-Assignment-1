import sys

sys.path.insert(
    0,
    r"c:\University\Second Year Programming\2AA4\2aa4-2026-base\assignments\visualize\catanatron",
)
from catanatron.models.map import BASE_MAP_TEMPLATE, initialize_tiles, CatanMap, NodeRef

tiles = initialize_tiles(BASE_MAP_TEMPLATE)
cmap = CatanMap.from_tiles(tiles)

valid_edges = set()
# In catanatron, an edge is usually a sorted tuple of two adjacent nodes on a hex
# Let's iterate over land tiles and get all adjacent node pairs
for tile in cmap.land_tiles.values():
    # adjacent pairs around a pointy-top hex:
    # N-NE, NE-SE, SE-S, S-SW, SW-NW, NW-N
    order = [
        NodeRef.NORTH,
        NodeRef.NORTHEAST,
        NodeRef.SOUTHEAST,
        NodeRef.SOUTH,
        NodeRef.SOUTHWEST,
        NodeRef.NORTHWEST,
    ]
    for i in range(6):
        n1 = tile.nodes[order[i]]
        n2 = tile.nodes[order[(i + 1) % 6]]
        edge = (min(n1, n2), max(n1, n2))
        valid_edges.add(edge)

print(f"Total valid edges: {len(valid_edges)}")

test_edges = [(13, 15), (13, 14), (14, 15)]
for e in test_edges:
    e_sort = (min(e[0], e[1]), max(e[0], e[1]))
    if e_sort in valid_edges:
        print(f"Edge {e_sort} IS valid!")
    else:
        print(f"Edge {e_sort} is NOT valid!")

print("All valid edges with 13:")
print([e for e in valid_edges if 13 in e])
print("All valid edges with 15:")
print([e for e in valid_edges if 15 in e])
