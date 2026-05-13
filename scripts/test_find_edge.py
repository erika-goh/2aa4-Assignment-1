import sys
import math

sys.path.insert(
    0,
    r"c:\University\Second Year Programming\2AA4\2aa4-2026-base\assignments\visualize\catanatron",
)
from catanatron.gym.envs.pygame_renderer import PygameRenderer
from catanatron.models.map import initialize_tiles, BASE_MAP_TEMPLATE, CatanMap
from catanatron.game import Game
from catanatron.models.player import Player, Color

tiles = initialize_tiles(BASE_MAP_TEMPLATE)
cmap = CatanMap.from_tiles(tiles)


def get_native_pos(node_id):
    import warnings

    warnings.filterwarnings("ignore")
    try:
        adj_tiles = cmap.adjacent_tiles[node_id]
        tile = adj_tiles[0]
        coord = next(k for k, v in cmap.land_tiles.items() if v == tile)
    except IndexError:
        tile = next(t for t in cmap.tiles.values() if node_id in t.nodes.values())
        coord = next(k for k, v in cmap.tiles.items() if v == tile)

    center_x, center_y = 500, 400
    q, s, r = coord
    RADIUS = 60
    HEIGHT = 2 * RADIUS
    WIDTH = math.sqrt(3) * RADIUS

    x = center_x + (WIDTH * (q + r / 2.0))
    y = center_y + (HEIGHT * (3.0 / 4.0) * r)

    noderef = next(k for k, v in tile.nodes.items() if v == node_id)

    dx, dy = 0, 0
    from catanatron.models.enums import NodeRef

    if noderef == NodeRef.NORTH:
        dy = -HEIGHT / 2.0
    elif noderef == NodeRef.SOUTH:
        dy = HEIGHT / 2.0
    elif noderef == NodeRef.NORTHEAST:
        dx = WIDTH / 2.0
        dy = -HEIGHT / 4.0
    elif noderef == NodeRef.SOUTHEAST:
        dx = WIDTH / 2.0
        dy = HEIGHT / 4.0
    elif noderef == NodeRef.NORTHWEST:
        dx = -WIDTH / 2.0
        dy = -HEIGHT / 4.0
    elif noderef == NodeRef.SOUTHWEST:
        dx = -WIDTH / 2.0
        dy = HEIGHT / 4.0

    return (x + dx, y + dy)


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

import networkx as nx

STATIC_GRAPH = nx.Graph()
for tile in cmap.tiles.values():
    if hasattr(tile, "edges"):
        STATIC_GRAPH.add_nodes_from(tile.nodes.values())
        STATIC_GRAPH.add_edges_from(tile.edges.values())

valid_edges = list(STATIC_GRAPH.edges())
edge_map = []

for u, v in java_connections:
    t_u = NODE_TRANSLATION[u]
    t_v = NODE_TRANSLATION[v]

    p_u = get_native_pos(t_u)
    p_v = get_native_pos(t_v)
    mid_x = (p_u[0] + p_v[0]) / 2.0
    mid_y = (p_u[1] + p_v[1]) / 2.0

    best_dist = 999999
    best_e = None
    for na, nb in valid_edges:
        n_p_a = get_native_pos(na)
        n_p_b = get_native_pos(nb)
        n_mid_x = (n_p_a[0] + n_p_b[0]) / 2.0
        n_mid_y = (n_p_a[1] + n_p_b[1]) / 2.0

        dist = math.hypot(n_mid_x - mid_x, n_mid_y - mid_y)
        if dist < best_dist:
            best_dist = dist
            best_e = (min(na, nb), max(na, nb))

    edge_map.append(
        f"edgeMapping.put(new EdgePair({min(u, v)}, {max(u, v)}), new int[]{{{best_e[0]}, {best_e[1]}}});"
    )

with open("edge_output.txt", "w") as f:
    f.write("\n".join(edge_map))
