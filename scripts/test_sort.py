import math

# We build standard coordinates for the Instructor board!
# Center is Tile 0.
# Hex math for pointy-topped where size = 1:
# W = 2 * (sqrt(3)/2)
# H = 2


def get_tile_centers():
    centers = {}
    # Cube: q, r, s
    # x = sqrt(3) * (q + r/2)
    # y = 3/2 * r
    # Map Tile ID to q, r
    coords = {
        0: (0, 0),
        1: (0, 1),  # SE: q=0, r=1
        2: (-1, 1),  # SW: q=-1, r=1
        3: (-1, 0),  # W: q=-1, r=0
        4: (0, -1),  # NW: q=0, r=-1
        5: (1, -1),  # NE: q=1, r=-1
        6: (1, 0),  # E: q=1, r=0
        7: (0, 2),  # SE of 1: q=0, r=2
        8: (-1, 2),  # SW of 1: q=-1, r=2
        9: (-2, 2),  # SW of 2: q=-2, r=2
        10: (-2, 1),  # W of 2: q=-2, r=1
        11: (-2, 0),  # W of 3: q=-2, r=0
        12: (-1, -1),  # NW of 3: q=-1, r=-1
        13: (0, -2),  # NW of 4: q=0, r=-2
        14: (1, -2),  # NE of 4: q=1, r=-2
        15: (2, -2),  # NE of 5: q=2, r=-2
        16: (2, -1),  # E of 5: q=2, r=-1
        17: (2, 0),  # E of 6: q=2, r=0
        18: (1, 1),  # SE of 6: q=1, r=1
    }
    for t, (q, r) in coords.items():
        cx = math.sqrt(3) * (q + r / 2.0)
        cy = 1.5 * r
        centers[t] = (cx, cy)
    return centers


centers = get_tile_centers()

# Vertex directions from tile center
# N, NE, SE, S, SW, NW
offsets = [
    (0, -1),  # N (Top)
    (math.sqrt(3) / 2, -0.5),  # NE (TopRight)
    (math.sqrt(3) / 2, 0.5),  # SE (BottomRight)
    (0, 1),  # S (Bottom)
    (-math.sqrt(3) / 2, 0.5),  # SW (BottomLeft)
    (-math.sqrt(3) / 2, -0.5),  # NW (TopLeft)
]

# The partially mapped lists from visual extraction
instructor_nodes = {
    0: [16, 19, 0, 1, 3, 15],
    1: [0, 20, 22, 23, 6, 2],
    2: [3, 2, 10, 11, 12, 13],
    3: [18, 15, 3, 13, 14, 17],
    4: [41, 42, 16, 15, 18, 39],
    5: [44, 45, 46, 19, 16, 42],
    6: [48, 49, 21, 20, 0, 19],
    7: [
        22,
        21,
        51,
        52,
        24,
        23,
    ],  # Wait! Let's ignore Ring 2, I'll derive Ring 2 using Pygame!
}

# In fact, I don't even need the visual numbers!!!
# If I just generate the graph using networkx,
# And assign the instructor IDs exactly!
# Wait! I can't generate the instructor IDs unless I know their pattern!
