def fx(ins, pt2=False):
    grid = [[0] * 1000 for _ in range(1000)]

    for i in ins:
        a, l, r = pre_p(i)
        x1, y1 = l
        x2, y2 = r

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if not pt2:
                    if a == "turn on":
                        grid[x][y] = 1
                    elif a == "turn off":
                        grid[x][y] = 0
                    elif a == "toggle":
                        grid[x][y] = 1 - grid[x][y]
                else:
                    if a == "turn on":
                        grid[x][y] += 1
                    elif a == "turn off":
                        grid[x][y] = max(0, grid[x][y] - 1)
                    elif a == "toggle":
                        grid[x][y] += 2

    if not pt2:
        count = sum(sum(row) for row in grid)
    else:
        count = sum(sum(row) for row in grid)

    return count


def pre_p(i):
    pts = i.split()
    if pts[0] == "toggle":
        a = "toggle"
        l = tuple(map(int, pts[1].split(',')))
        r = tuple(map(int, pts[3].split(',')))
    else:
        a = pts[0] + " " + pts[1]
        l = tuple(map(int, pts[2].split(',')))
        r = tuple(map(int, pts[4].split(',')))
    return a, l, r


ins = [line for line in open('input6.txt').read().strip().split("\n")]
print(fx(ins, pt2=False))
print(fx(ins, pt2=True))
