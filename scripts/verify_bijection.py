translation = [
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

print(f"Length: {len(translation)}")
is_valid = True
if len(set(translation)) != 54:
    print("ERROR: Duplicates found!")
    is_valid = False
for i in range(54):
    if i not in translation:
        print(f"ERROR: Missing {i}")
        is_valid = False

if is_valid:
    print(
        "SUCCESS: The translation array is a perfect 54-element bijection/permutation of 0-53."
    )
