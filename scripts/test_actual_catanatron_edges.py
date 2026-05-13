import sys

sys.path.insert(
    0,
    r"c:\University\Second Year Programming\2AA4\2aa4-2026-base\assignments\visualize\catanatron",
)
from catanatron.models.map import BASE_MAP_TEMPLATE, initialize_tiles, CatanMap
from catanatron.game import Game

tiles = initialize_tiles(BASE_MAP_TEMPLATE)
cmap = CatanMap.from_tiles(tiles)

from catanatron.models.player import Player, Color

game = Game([Player(Color.RED), Player(Color.BLUE)])  # Initialize default game
board = game.state.board

# Actually, CatanMap calculates edges!
print("CatanMap true edges:")
true_edges = cmap.edges
print(list(true_edges)[:10])

# Let's see what edges contain 13, 14, 15
print("Edges with 13:", [e for e in true_edges if 13 in e])
print("Edges with 14:", [e for e in true_edges if 14 in e])
print("Edges with 15:", [e for e in true_edges if 15 in e])

# Also let's print the dict value of cmap.nodes[13], etc to see coordinates
print("Node 13 coordinate:", cmap.nodes[13].coordinate)
print("Node 14 coordinate:", cmap.nodes[14].coordinate)
print("Node 15 coordinate:", cmap.nodes[15].coordinate)
