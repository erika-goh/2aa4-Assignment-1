import sys
import networkx as nx

sys.path.insert(
    0,
    r"c:\University\Second Year Programming\2AA4\2aa4-2026-base\assignments\visualize\catanatron",
)
from catanatron.models.map import initialize_tiles, BASE_MAP_TEMPLATE, CatanMap

# 1. Target Graph (Catanatron)
tiles = initialize_tiles(BASE_MAP_TEMPLATE)
cmap = CatanMap.from_tiles(tiles)
NATIVE_GRAPH = nx.Graph()
for tile in cmap.tiles.values():
    if hasattr(tile, "edges"):
        NATIVE_GRAPH.add_edges_from(tile.edges.values())

# 2. Source Graph (User's Corrected Backend)
java_connections = [
    [0, 1],
    [0, 5],
    [0, 20],
    [1, 2],
    [1, 6],
    [2, 3],
    [2, 9],
    [3, 4],
    [3, 12],
    [4, 5],
    [4, 15],
    [5, 16],
    [6, 7],
    [6, 23],
    [7, 8],
    [7, 24],
    [8, 9],
    [8, 27],
    [9, 10],
    [10, 11],
    [10, 29],
    [11, 12],
    [11, 32],
    [12, 13],
    [13, 14],
    [13, 34],
    [14, 15],
    [14, 37],
    [15, 17],
    [16, 5],
    [16, 18],
    [16, 21],
    [17, 39],
    [17, 18],
    [18, 40],
    [19, 20],
    [19, 46],
    [19, 21],
    [20, 0],
    [20, 22],
    [21, 43],
    [22, 23],
    [22, 49],
    [23, 52],
    [24, 25],
    [24, 53],
    [25, 26],
    [26, 27],
    [27, 28],
    [28, 29],
    [29, 30],
    [30, 31],
    [31, 32],
    [32, 33],
    [33, 34],
    [34, 36],
    [35, 37],
    [35, 39],
    [36, 37],
    [38, 39],
    [38, 42],
    [40, 41],
    [40, 42],
    [41, 43],
    [43, 44],
    [44, 45],
    [45, 46],
    [46, 47],
    [47, 48],
    [48, 49],
    [49, 50],
    [50, 51],
    [51, 52],
    [52, 53],
]
BACKEND_GRAPH = nx.Graph()
BACKEND_GRAPH.add_edges_from(java_connections)

# 3. Current Mapping (NODE_TRANSLATION)
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


# Check if current mapping preserves edges
def check_mapping(mapping):
    broken = []
    for u, v in java_connections:
        tu, tv = mapping[u], mapping[v]
        if not NATIVE_GRAPH.has_edge(tu, tv):
            broken.append((u, v, tu, tv))
    return broken


broken = check_mapping(NODE_TRANSLATION)
print(f"Current mapping breaks {len(broken)} edges out of {len(java_connections)}.")
if broken:
    print("Examples of broken edges (Backend Edge -> Native Nodes):")
    for u, v, tu, tv in broken[:5]:
        print(f"  ({u}, {v}) -> ({tu}, {tv})")

# 4. Find the correct isomorphism
print("\nSearching for valid isomorphism...")
GM = nx.algorithms.isomorphism.GraphMatcher(NATIVE_GRAPH, BACKEND_GRAPH)
if GM.is_isomorphic():
    print("Graphs are isomorphic!")
    # mapping is from NATIVE to BACKEND. We want BACKEND to NATIVE.
    mapping_native_to_backend = GM.mapping
    mapping_backend_to_native = {v: k for k, v in mapping_native_to_backend.items()}

    # Check if we can improve it to match known visual positions
    # (Actually, let's just find ONE that matches 14->13 and 15->14 sequence logic if possible)
    # The user said settlement 14 worked visually.
    # From Step 515: 14 was at 15, 15 was at 13 in the "wrong" state?
    # Wait, let's just output the first valid one and verify a few nodes.

    new_translation = [mapping_backend_to_native[i] for i in range(54)]
    print("\nNew NODE_TRANSLATION array proposal:")
    print(new_translation)

    # Verify proposal
    proposal_broken = check_mapping(new_translation)
    print(f"Proposed mapping breaks {len(proposal_broken)} edges.")
else:
    print("Graphs are NOT isomorphic. Scaling node translation alone cannot fix this.")
