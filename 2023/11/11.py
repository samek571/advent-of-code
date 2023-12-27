from itertools import accumulate

def expand(line, gap):
    empty = [gap - 1] * (max(line) + 1)
    for n in line:
        empty[n] = 0
    
    add = list(accumulate(empty)) #prefix sum if that aint clear

    return [n + add[n] for n in line]


def fnx(s, gap):
    matrix = []
    for line in open(s).read().split("\n")[:-1]:
        matrix.append([i for i in line])
    
    galaxies = [[x, y] for y, line in enumerate(matrix) for x, char in enumerate(line) if char == '#']

    x = expand([a for a,b in galaxies], gap)
    y = expand([b for a,b in galaxies], gap)
    galaxies = [(x[i], y[i]) for i in range(len(x))]

    res = 0
    for fx, fy in galaxies:
        for sx, sy in galaxies:
            res += abs(fy-sy) + abs(sx-fx)

    return res // 2

print(fnx('input11h.txt', 2))
print(fnx('input11h.txt', 10))
print(fnx('input11h.txt', 100))
print(fnx('input11.txt', 1000000))