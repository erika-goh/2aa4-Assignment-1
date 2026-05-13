import sys

# Java Canonical Hex Definitions (Visual mapping based on User's Canonical logic)
# Center = Tile 0
# TR = Tile 1
# TL = Tile 2
# Left = Tile 3
# BL = Tile 4
# BR = Tile 5
# Right = Tile 6
# Outer ring starts TR, goes counter-clockwise?
# Wait, let's look at the mapping logic in Java to confirm Hex positions.

java_canonical = [
    [5, 0, 1, 2, 3, 4],  # Tile 0: Center
    [1, 6, 7, 8, 9, 2],  # Tile 1: TR
    [3, 2, 9, 10, 11, 12],  # Tile 2: TL
    [15, 4, 3, 12, 13, 14],  # Tile 3: L
    [18, 16, 5, 4, 15, 17],  # Tile 4: BL
    [21, 19, 20, 0, 5, 16],  # Tile 5: BR
    [20, 22, 23, 6, 1, 0],  # Tile 6: R
    [7, 24, 25, 26, 27, 8],  # Tile 7: Outer TR-ish? Let's trace it.
]

# We know Java Center is C0=5, C1=0, C2=1, C3=2, C4=3, C5=4
# So Java C0 is Top-Left (NW), C1 is Top (N), C2 is Top-Right (NE)...
# Let's map Java Node IDs to physical coordinates!
# Let Center point be (0,0).
import math

hex_size = 1.0
w = math.sqrt(3) * hex_size
h = 2 * hex_size

# Java Hex offsets (assuming Pointy Topped)
# Center: 0, 0
# TR: x=w/2, y=-0.75*h (Wait, is it pointy topped? Nodes are NW, N, NE. So flat top? No, N is a node, so it's Pointy Topped.
# If pointy topped, centers are separated by:
# TR: dx = w/2, dy = -0.75*h

# Instead of math, let's just use topology logic!
# Java Tile 0 shares nodes with Java Tile 1.
# Tile 0: [5, 0, 1, 2, 3, 4]
# Tile 1: [1, 6, 7, 8, 9, 2]
# Shared nodes: 1 and 2.
# In Tile 0, 1 is NE, 2 is SE.
# In Tile 1, 1 is NW (C0), 2 is SW (C5).
# So Tile 1 is located EXACTLY at the NORTHEAST of Center! So Tile 1 is TR (Top-Right).

# Tile 0: [5, 0, 1, 2, 3, 4]
# Tile 2: [3, 2, 9, 10, 11, 12]
# Shared: 2 and 3.
# In Tile 0, 2 is SE, 3 is S.
# In Tile 2, 3 is NW (C0), 2 is N (C1).
# So Tile 2 (TL?) Wait! If Tile 2 shares SE and S of Center...
# That means Tile 2 is SOUTHEAST of Center! (Bottom-Right!!!)
# Let's re-verify:
# Tile 0 SE is 2, S is 3.
# Tile 2 NW is 3, N is 2.
# If Center SE touches Tile 2 N, it's impossible for a hexagon.
# Wait! In Tile 0, 2 is C3 (SE).
# In Tile 2, 2 is C1 (N).
# So Center's SE node is the same as Tile 2's N node.
# And Center's S node (3) is Tile 2's NW node (3).
# If Center SE == Tile 2 N, and Center S == Tile 2 NW:
# Tile 2 MUST BE directly SOUTHEAST of Center!! (Bottom-Right!!)

# Let's test this in Catanatron coordinates!
print("Run this to analyze topology")
