import sys
import re

with open(
    r"c:\University\Second Year Programming\2AA4\2aa4-Assignment-1\edge_output.txt", "r"
) as f:
    content = f.read().strip()

lines = content.split("\n")
map_lines = []
for line in lines:
    if "EdgePair" in line:
        # e.g.: edgeMapping.put(new EdgePair(0, 1), new int[]{1, 2});
        match = re.search(
            r"EdgePair\((\d+), (\d+)\), new int\[\]\{(\d+), (\d+)\}", line
        )
        if match:
            u, v, nu, nv = match.groups()
            map_lines.append(
                f'        EDGE_TRANSLATION.put("{u}_{v}", new int[]{{{nu}, {nv}}});'
            )

map_code = "\n".join(map_lines)

java_file = r"c:\University\Second Year Programming\2AA4\2aa4-Assignment-1\src-gen\catandomainmodel\GameStateExporter.java"
with open(java_file, "r") as f:
    java_cod = f.read()

# insert EDGE_TRANSLATION definition after NODE_TRANSLATION
insertion_point = "    };\n"
idx = java_cod.find(insertion_point, java_cod.find("NODE_TRANSLATION"))
if idx != -1:
    idx += len(insertion_point)
    new_code = (
        java_cod[:idx]
        + "\n    private static final java.util.Map<String, int[]> EDGE_TRANSLATION = new java.util.HashMap<>();\n    static {\n"
        + map_code
        + "\n    }\n"
        + java_cod[idx:]
    )

    # Now replace the writeRoadsJson part
    old_road_part = """                sb.append(JSON_START_BRACE)
                        .append(\"\\\"a\\\": \").append(nodeA).append(\", \")
                        .append(\"\\\"b\\\": \").append(nodeB).append(\", \")
                        .append(\"\\\"owner\\\": \\\"\").append(color).append(\"\\\"\")
                        .append(\"}\");"""

    new_road_part = """                int minNode = Math.min(nodeA, nodeB);
                int maxNode = Math.max(nodeA, nodeB);
                int[] transEdge = EDGE_TRANSLATION.get(minNode + "_" + maxNode);
                if (transEdge == null) transEdge = new int[]{nodeA, nodeB}; // fallback
                sb.append(JSON_START_BRACE)
                        .append(\"\\\"a\\\": \").append(transEdge[0]).append(\", \")
                        .append(\"\\\"b\\\": \").append(transEdge[1]).append(\", \")
                        .append(\"\\\"owner\\\": \\\"\").append(color).append(\"\\\"\")
                        .append(\"}\");"""

    new_code = new_code.replace(old_road_part, new_road_part)

    with open(java_file, "w") as fw:
        fw.write(new_code)
    print("Patched GameStateExporter.java successfully.")
else:
    print("Failed to find insertion point.")
