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
        match = re.search(
            r"EdgePair\((\d+), (\d+)\), new int\[\]\{(\d+), (\d+)\}", line
        )
        if match:
            u, v, nu, nv = match.groups()
            map_lines.append(
                f'        EDGE_TRANSLATION.put("{u}_{v}", new int[]{{{nu}, {nv}}});'
            )

map_code = "\n".join(map_lines)
dict_code = (
    "\n    private static final java.util.Map<String, int[]> EDGE_TRANSLATION = new java.util.HashMap<>();\n    static {\n"
    + map_code
    + "\n    }\n"
)

java_file = r"c:\University\Second Year Programming\2AA4\2aa4-Assignment-1\src-gen\catandomainmodel\GameStateExporter.java"
with open(java_file, "r") as f:
    java_cod = f.read()

# Insert the dictionary right before baseMapPath declaration
java_cod = re.sub(
    r"(    private String baseMapPath;)",
    lambda m: dict_code + "\n" + m.group(1),
    java_cod,
)

# Replace the formatting block inside writeRoadsJson
old_block_pattern = r'String color = mapPlayerToColor\(e\.getRoad\(\)\.getOwner\(\)\.getId\(\)\);\s*sb\.append\(JSON_START_BRACE\)\s*\.append\("\"a\": "\)\.append\(nodeA\)\.append\(", "\)\s*\.append\("\"b\": "\)\.append\(nodeB\)\.append\(", "\)\s*\.append\("\"owner\": \""\)\.append\(color\)\.append\("\""\)\s*\.append\("}"\);'

new_block = """String color = mapPlayerToColor(e.getRoad().getOwner().getId());
                int minNode = Math.min(nodeA, nodeB);
                int maxNode = Math.max(nodeA, nodeB);
                int[] transEdge = EDGE_TRANSLATION.get(minNode + "_" + maxNode);
                if (transEdge == null) transEdge = new int[]{nodeA, nodeB};
                sb.append(JSON_START_BRACE)
                        .append(\"\\\"a\\\": \").append(transEdge[0]).append(\", \")
                        .append(\"\\\"b\\\": \").append(transEdge[1]).append(\", \")
                        .append(\"\\\"owner\\\": \\\"\").append(color).append(\"\\\"\")
                        .append(\"}\");"""

java_cod = re.sub(old_block_pattern, new_block, java_cod)

with open(java_file, "w") as fw:
    fw.write(java_cod)

print("Patched GameStateExporter.java V2 successfully.")
