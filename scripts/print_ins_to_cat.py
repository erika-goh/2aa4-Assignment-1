import sys

sys.path.insert(
    0,
    r"c:\University\Second Year Programming\2AA4\2aa4-2026-base\assignments\visualize\catanatron",
)
from catanatron.models.map import BASE_MAP_TEMPLATE, initialize_tiles, CatanMap, NodeRef

instructor_nodes = {
    0: [5, 0, 1, 2, 3, 4],
    1: [1, 6, 7, 8, 9, 2],
    2: [3, 2, 9, 10, 11, 12],
    3: [15, 4, 3, 12, 13, 14],
    4: [18, 16, 5, 4, 15, 17],
    5: [21, 19, 20, 0, 5, 16],
    6: [20, 22, 23, 6, 1, 0],
    7: [7, 24, 25, 26, 27, 8],
    8: [9, 8, 27, 28, 29, 10],
    9: [11, 10, 29, 30, 31, 32],
    10: [13, 12, 11, 32, 33, 34],
    11: [37, 14, 13, 34, 35, 36],
    12: [39, 17, 15, 14, 37, 38],
    13: [42, 40, 18, 17, 39, 41],
    14: [44, 43, 21, 16, 18, 40],
    15: [45, 47, 46, 19, 21, 43],
    16: [46, 48, 49, 22, 20, 19],
    17: [49, 50, 51, 52, 23, 22],
    18: [23, 52, 53, 24, 7, 6],
}
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

tiles = initialize_tiles(BASE_MAP_TEMPLATE)
cmap = CatanMap.from_tiles(tiles)
tile_map = {coord: tile for coord, tile in cmap.land_tiles.items()}

dir_map = [
    NodeRef.NORTH,
    NodeRef.NORTHEAST,
    NodeRef.SOUTHEAST,
    NodeRef.SOUTH,
    NodeRef.SOUTHWEST,
    NodeRef.NORTHWEST,
]
ins_to_cat = {}

for i in range(19):
    t_nodes = instructor_nodes[i]
    cat_tile = tile_map[coords[i]]
    for j in range(6):
        ins_id = t_nodes[j]
        cat_id = cat_tile.nodes[dir_map[j]]
        if ins_id in ins_to_cat and ins_to_cat[ins_id] != cat_id:
            print(
                f"CONFLICT! Instructor {ins_id} mapped to {ins_to_cat[ins_id]} and {cat_id} at tile {i}"
            )
        ins_to_cat[ins_id] = cat_id

for i in [13, 14, 15]:
    try:
        print(f"Instructor Node {i} -> Catanatron Native Node {ins_to_cat[i]}")
    except:
        pass
