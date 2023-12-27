import collections


def pre_p(s):
    origin = []
    matrix = []
    for i, line in enumerate(open(s).read().strip().split("\n")):
        matrix.append([h for h in line])
        if "S" in line:
            origin = [i, line.index("S")]

    return origin, matrix


def fx(s, ttl):
    (i,j), matrix = pre_p(s)
    q = collections.deque([(i,j,ttl)])
    seen = set()
    res = 0
    while q:
        x, y, ttl = q.popleft()

        if (x, y) in seen or ttl<0: continue
        seen.add((x, y))

        if ttl%2==0:
            res+=1

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] != "#":
                q.append((nx, ny, ttl-1))

    return res


#i think the key was to realize every even step is counted towards the possible ending point
print(fx('input21h.txt', 6))
print(fx('input21.txt', 64))