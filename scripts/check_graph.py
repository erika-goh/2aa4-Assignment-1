import sys

sys.path.append(
    r"c:\University\Second Year Programming\2AA4\2aa4-2026-base\assignments\visualize\catanatron\catanatron"
)
from catanatron.models.board import STATIC_GRAPH

land_nodes = set(range(54))
edges = list(STATIC_GRAPH.subgraph(land_nodes).edges())

print("EXACT 72 LAND EDGES OF STATIC_GRAPH:")
output = []
for edge in sorted([tuple(sorted(e)) for e in edges]):
    output.append(f"{{{edge[0]}, {edge[1]}}}")

print(", ".join(output))
