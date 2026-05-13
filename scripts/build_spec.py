import sys
import os

# Actual Catanatron unit vectors:
DIRECTIONS = {
    "SE": (0, -1, 1),
    "SW": (-1, 0, 1),
    "W": (-1, 1, 0),
    "NW": (0, 1, -1),
    "NE": (1, 0, -1),
    "E": (1, -1, 0),
}


def add_coord(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1], c1[2] + c2[2])


def scale(c, s):
    return (c[0] * s, c[1] * s, c[2] * s)


# Instructor ring start
TILE_COORDS = []
TILE_COORDS.append((0, 0, 0))  # 0

# Ring 1
TILE_COORDS.append(DIRECTIONS["SE"])  # 1
TILE_COORDS.append(DIRECTIONS["SW"])  # 2
TILE_COORDS.append(DIRECTIONS["W"])  # 3
TILE_COORDS.append(DIRECTIONS["NW"])  # 4
TILE_COORDS.append(DIRECTIONS["NE"])  # 5
TILE_COORDS.append(DIRECTIONS["E"])  # 6

# Ring 2
TILE_COORDS.append(scale(DIRECTIONS["SE"], 2))  # 7
TILE_COORDS.append(add_coord(scale(DIRECTIONS["SE"], 2), DIRECTIONS["W"]))  # 8
TILE_COORDS.append(scale(DIRECTIONS["SW"], 2))  # 9
TILE_COORDS.append(add_coord(scale(DIRECTIONS["SW"], 2), DIRECTIONS["NW"]))  # 10
TILE_COORDS.append(scale(DIRECTIONS["W"], 2))  # 11
TILE_COORDS.append(add_coord(scale(DIRECTIONS["W"], 2), DIRECTIONS["NE"]))  # 12
TILE_COORDS.append(scale(DIRECTIONS["NW"], 2))  # 13
TILE_COORDS.append(add_coord(scale(DIRECTIONS["NW"], 2), DIRECTIONS["E"]))  # 14
TILE_COORDS.append(scale(DIRECTIONS["NE"], 2))  # 15
TILE_COORDS.append(add_coord(scale(DIRECTIONS["NE"], 2), DIRECTIONS["SE"]))  # 16
TILE_COORDS.append(scale(DIRECTIONS["E"], 2))  # 17
TILE_COORDS.append(add_coord(scale(DIRECTIONS["E"], 2), DIRECTIONS["SW"]))  # 18

hex_to_nodes = {}
for coord in TILE_COORDS:
    # Catanatron dynamic generation iterates in N, NE, SE, S, SW, NW.
    # N meets NW, NE
    n_set = tuple(
        sorted(
            [
                coord,
                add_coord(coord, DIRECTIONS["NW"]),
                add_coord(coord, DIRECTIONS["NE"]),
            ]
        )
    )
    # NE meets NE, E
    ne_set = tuple(
        sorted(
            [
                coord,
                add_coord(coord, DIRECTIONS["NE"]),
                add_coord(coord, DIRECTIONS["E"]),
            ]
        )
    )
    # SE meets E, SE
    se_set = tuple(
        sorted(
            [
                coord,
                add_coord(coord, DIRECTIONS["E"]),
                add_coord(coord, DIRECTIONS["SE"]),
            ]
        )
    )
    # S meets SE, SW
    s_set = tuple(
        sorted(
            [
                coord,
                add_coord(coord, DIRECTIONS["SE"]),
                add_coord(coord, DIRECTIONS["SW"]),
            ]
        )
    )
    # SW meets SW, W
    sw_set = tuple(
        sorted(
            [
                coord,
                add_coord(coord, DIRECTIONS["SW"]),
                add_coord(coord, DIRECTIONS["W"]),
            ]
        )
    )
    # NW meets W, NW
    nw_set = tuple(
        sorted(
            [
                coord,
                add_coord(coord, DIRECTIONS["W"]),
                add_coord(coord, DIRECTIONS["NW"]),
            ]
        )
    )

    hex_to_nodes[coord] = [n_set, ne_set, se_set, s_set, sw_set, nw_set]

node_to_id = {}
next_id = 0

for i, coord in enumerate(TILE_COORDS):
    for node in hex_to_nodes[coord]:
        if node not in node_to_id:
            node_to_id[node] = next_id
            next_id += 1

print("NEW TILES MAPPING:")
for i, coord in enumerate(TILE_COORDS):
    ids = [node_to_id[n] for n in hex_to_nodes[coord]]
    print(f"Tile {i}: {ids}")

edges = set()
for coord in TILE_COORDS:
    ids = [node_to_id[n] for n in hex_to_nodes[coord]]
    for j in range(6):
        a = ids[j]
        b = ids[(j + 1) % 6]
        edges.add(tuple(sorted([a, b])))

print("EDGES:")
output = []
for idx, e in enumerate(sorted(list(edges))):
    output.append(f"{{{e[0]}, {e[1]}}}")
print(", ".join(output))

print("GameStateExporter coords array:")
for i, c in enumerate(TILE_COORDS):
    print(f"  {{{c[0]}, {c[1]}, {c[2]}}}, // Tile {i}")
