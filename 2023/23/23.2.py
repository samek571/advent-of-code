#https://en.wikipedia.org/wiki/Edge_contraction
import sys
sys.setrecursionlimit(1000000)

s='input23.txt'
lines = [line for line in open(s).read().strip().split("\n")]
edges = {}

for i, line in enumerate(lines):
    for j, v in enumerate(line):
        if v in ".>v":
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                x, y = i+dx, j+dy

                if 0 <= x < len(lines) and 0 <= y < len(line) and lines[x][y] in ".>v":
                    edges.setdefault((i, j), set()).add((x, y, 1))
                    edges.setdefault((x, y), set()).add((i, j, 1))


while True:
    for n, e in edges.items():
        if len(e) == 2:
            a, b = e
            edges[a[:2]].remove(n + (a[2],))
            edges[b[:2]].remove(n + (b[2],))
            edges[a[:2]].add((b[0], b[1], a[2] + b[2]))
            edges[b[:2]].add((a[0], a[1], a[2] + b[2]))
            del edges[n]
            break
    else:
        break


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

    for x, y, l in edges[(i, j)]:
        dfs(x, y, d + l)

    visited.remove((i, j))

print(dfs(0, 1, 0))
