import sys
import networkx as nx

sys.path.insert(
    0,
    r"c:\University\Second Year Programming\2AA4\2aa4-2026-base\assignments\visualize\catanatron",
)
from catanatron.models.map import initialize_tiles, BASE_MAP_TEMPLATE, CatanMap

with open("audit_result.txt", "w") as f:
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

    f.write(
        f"Native Graph: {NATIVE_GRAPH.number_of_nodes()} nodes, {NATIVE_GRAPH.number_of_edges()} edges\n"
    )
    f.write(
        f"Backend Graph: {BACKEND_GRAPH.number_of_nodes()} nodes, {BACKEND_GRAPH.number_of_edges()} edges\n"
    )

    def get_degree_seq(G):
        return sorted([d for n, d in G.degree()])

    n_deg = get_degree_seq(NATIVE_GRAPH)
    b_deg = get_degree_seq(BACKEND_GRAPH)
    f.write(f"Native Degree Seq: {n_deg}\n")
    f.write(f"Backend Degree Seq: {b_deg}\n")

    if n_deg != b_deg:
        f.write("\nDegree sequences DO NOT MATCH. The graphs are NOT isomorphic.\n")
    else:
        f.write("\nDegree sequences match. Graphs might be isomorphic.\n")

    # Check if current NODE_TRANSLATION is an isomorphism
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
    broken = []
    for u, v in java_connections:
        tu, tv = NODE_TRANSLATION[u], NODE_TRANSLATION[v]
        if not NATIVE_GRAPH.has_edge(tu, tv):
            broken.append((u, v, tu, tv))

    f.write(f"Current mapping breaks {len(broken)} edges.\n")
    if broken:
        f.write("Broken edges:\n")
        for u, v, tu, tv in broken:
            f.write(f"  ({u}, {v}) -> ({tu}, {tv})\n")
