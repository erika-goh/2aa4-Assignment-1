import sys
import os

sys.path.insert(
    0,
    r"c:\University\Second Year Programming\2AA4\2aa4-2026-base\assignments\visualize\catanatron",
)
from catanatron.models.map import BASE_MAP_TEMPLATE, initialize_tiles, CatanMap

tiles = initialize_tiles(BASE_MAP_TEMPLATE)
cmap = CatanMap.from_tiles(tiles)

import networkx as nx

STATIC_GRAPH = nx.Graph()
for tile in cmap.tiles.values():
    STATIC_GRAPH.add_nodes_from(tile.nodes.values())
    STATIC_GRAPH.add_edges_from(tile.edges.values())

sg = STATIC_GRAPH.subgraph(range(54))

edges_str = []
for a, b in sg.edges():
    edges_str.append(f"{{{a}, {b}}}")

print("EDGES:")
print(", ".join(edges_str))

print("\nTILES:")
for coord, tile in cmap.land_tiles.items():
    # Only map land nodes for the tile
    land_nodes = {k: v for k, v in tile.nodes.items() if v < 54}
    print(f"Tile {tile.id} (q={coord[0]}, s={coord[1]}, r={coord[2]}): {land_nodes}")

# Let's map coordinates exactly as they exist in GameStateExporter
coords_order = [
    [0, 0, 0],
    [1, -1, 0],
    [1, 0, -1],
    [0, 1, -1],
    [-1, 1, 0],
    [-1, 0, 1],
    [0, -1, 1],
    [2, -2, 0],
    [2, -1, -1],
    [2, 0, -2],
    [1, 1, -2],
    [0, 2, -2],
    [-1, 2, -1],
    [-2, 2, 0],
    [-2, 1, 1],
    [-2, 0, 2],
    [-1, -1, 2],
    [0, -2, 2],
    [1, -2, 1],
]

for coord in coords_order:
    for ccoord, tile in cmap.land_tiles.items():
        if list(ccoord) == coord:
            print(f"Index for GameStateExporter coords {coord}: Tile {tile.id}")
