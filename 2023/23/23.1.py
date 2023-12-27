import sys
sys.setrecursionlimit(1000000)

s='input23.txt'
lines = [line for line in open(s).read().strip().split("\n")]
edges = {}

for i, line in enumerate(lines):
    for j, v in enumerate(line):
        if v == ".":
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                x, y = i+dx, j+dy
                if 0 <= x < len(lines) and 0 <= y < len(line) and lines[x][y] == ".":
                    edges.setdefault((i, j), set()).add((x, y))
                    edges.setdefault((x, y), set()).add((i, j))

        elif v == ">":
            edges.setdefault((i, j), set()).add((i, j+1))
            edges.setdefault((i, j-1), set()).add((i, j))
        elif v == "v":
            edges.setdefault((i, j), set()).add((i+1, j))
            edges.setdefault((i-1, j), set()).add((i, j))


n, m = len(lines), len(lines[0])
res = 0
visited = set()
def dfs(i, j, d):
    global res

    if (i, j) == (n-1, m-2):
        res = max(res, d)
        return

    if (i, j) in visited:
        return

    visited.add((i, j))

    for x, y in edges[(i, j)]:
        dfs(x, y, d + 1)

    visited.remove((i, j))

dfs(0, 1, 0)
print(res)