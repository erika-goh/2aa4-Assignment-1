mapping = {
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

edges = set()
nodes = set()
for m in mapping.values():
    for i in range(6):
        u, v = m[i], m[(i + 1) % 6]
        edges.add(tuple(sorted((u, v))))
        nodes.add(u)

sorted_edges = sorted(list(edges))

with open("edges_output.txt", "w") as f:
    f.write(f"Total nodes: {len(nodes)}\n")
    f.write(f"Total edges: {len(sorted_edges)}\n")
    f.write("Edges array for Java:\n")
    for i in range(0, len(sorted_edges), 9):
        chunk = sorted_edges[i : i + 9]
        line = ", ".join([f"{{ {u}, {v} }}" for u, v in chunk])
        f.write("                " + line + ",\n")
