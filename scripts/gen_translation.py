import json

canonical = [
    [5, 0, 1, 2, 3, 4],  # Tile 0
    [1, 6, 7, 8, 9, 2],  # Tile 1
    [3, 2, 9, 10, 11, 12],  # Tile 2
    [15, 4, 3, 12, 13, 14],  # Tile 3
    [18, 16, 5, 4, 15, 17],  # Tile 4
    [21, 19, 20, 0, 5, 16],  # Tile 5
    [20, 22, 23, 6, 1, 0],  # Tile 6
    [7, 24, 25, 26, 27, 8],  # Tile 7
    [9, 8, 27, 28, 29, 10],  # Tile 8
    [11, 10, 29, 30, 31, 32],  # Tile 9
    [13, 12, 11, 32, 33, 34],  # Tile 10
    [37, 14, 13, 34, 35, 36],  # Tile 11
    [39, 17, 15, 14, 37, 38],  # Tile 12
    [42, 40, 18, 17, 39, 41],  # Tile 13
    [44, 43, 21, 16, 18, 40],  # Tile 14
    [45, 47, 46, 19, 21, 43],  # Tile 15
    [46, 48, 49, 22, 20, 19],  # Tile 16
    [49, 50, 51, 52, 23, 22],  # Tile 17
    [23, 52, 53, 24, 7, 6],  # Tile 18
]

true_native = [
    [0, 1, 2, 3, 4, 5],  # Tile 0
    [2, 6, 7, 8, 9, 3],  # Tile 1
    [4, 3, 9, 10, 11, 12],  # Tile 2
    [13, 5, 4, 12, 14, 15],  # Tile 3
    [16, 17, 0, 5, 13, 18],  # Tile 4
    [19, 20, 21, 1, 0, 17],  # Tile 5
    [21, 22, 23, 6, 2, 1],  # Tile 6
    [7, 24, 25, 26, 27, 8],  # Tile 7
    [9, 8, 27, 28, 29, 10],  # Tile 8
    [11, 10, 29, 30, 31, 32],  # Tile 9
    [14, 12, 11, 32, 33, 34],  # Tile 10
    [35, 15, 14, 34, 36, 37],  # Tile 11
    [38, 18, 13, 15, 35, 39],  # Tile 12
    [40, 41, 16, 18, 38, 42],  # Tile 13
    [43, 44, 19, 17, 16, 41],  # Tile 14
    [45, 46, 47, 20, 19, 44],  # Tile 15
    [47, 48, 49, 22, 21, 20],  # Tile 16
    [49, 50, 51, 52, 23, 22],  # Tile 17
    [23, 52, 53, 24, 7, 6],  # Tile 18
]

java_to_cat = {}
for i in range(19):
    for j in range(6):
        java_id = canonical[i][j]
        cat_id = true_native[i][j]
        if java_id in java_to_cat and java_to_cat[java_id] != cat_id:
            print(
                f"CONFLICT AT {java_id}: mapped to {java_to_cat[java_id]} and {cat_id}"
            )
        java_to_cat[java_id] = cat_id

array_str = "int[] javaToCatanatron = {\n    "
for i in range(54):
    array_str += f"{java_to_cat.get(i, -1)}, "
    if (i + 1) % 10 == 0:
        array_str += "\n    "
array_str += "\n};"
print(array_str)
