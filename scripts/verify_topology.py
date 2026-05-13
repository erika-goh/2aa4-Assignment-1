import sys

sys.path.insert(
    0,
    r"c:\University\Second Year Programming\2AA4\2aa4-2026-base\assignments\visualize\catanatron",
)
from catanatron.models.map import initialize_tiles, BASE_MAP_TEMPLATE, CatanMap
import networkx as nx

tiles = initialize_tiles(BASE_MAP_TEMPLATE)
cmap = CatanMap.from_tiles(tiles)

STATIC_GRAPH = nx.Graph()
for tile in cmap.tiles.values():
    if hasattr(tile, "edges"):
        STATIC_GRAPH.add_nodes_from(tile.nodes.values())
        STATIC_GRAPH.add_edges_from(tile.edges.values())

NODE_TRANSLATION = [
    1,
    2,
    3,
    4,
    5,
    0,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    14,
    15,
    13,
    17,
    18,
    16,
    20,
    21,
    19,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    36,
    37,
    35,
    39,
    38,
    41,
    42,
    40,
    44,
    43,
    45,
    47,
    46,
    48,
    49,
    50,
    51,
    52,
    53,
]


def check_edge(u, v):
    tu, tv = NODE_TRANSLATION[u], NODE_TRANSLATION[v]
    valid = STATIC_GRAPH.has_edge(tu, tv)
    print(
        f"Backend edge ({u}, {v}) -> Visualizer nodes ({tu}, {tv}): {'VALID' if valid else 'INVALID'}"
    )
    return valid


print("Testing requested edges:")
check_edge(14, 15)
check_edge(0, 1)

print("\nTesting other edges from user's list:")
check_edge(0, 5)
check_edge(0, 20)
check_edge(1, 2)
check_edge(1, 6)
