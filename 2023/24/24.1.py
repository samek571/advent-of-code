import re

def pre_p(s):
    hailstones = []

    for line in open(s).read().strip().split("\n"):
        x, y, z, vx, vy, vz = list(map(int, re.findall('-?[0-9]+', line))) #fucking forgot about negative sign
        slope = vy / vx
        meet = y - slope * x
        hailstones.append((x, y, z, vx, vy, vz, slope, meet))

    return hailstones



def fx(s, mini, maxi):
    hailstones = pre_p(s)
    res = 0
    for h1 in hailstones:
        for h2 in hailstones:
            if h1 != h2:

                #identical slopes == parallel lines
                if h1[-2] == h2[-2]: continue

                x = (h2[-1] - h1[-1]) / (h1[-2] - h2[-2])
                y = h1[-2] * x + h1[-1]
                t1 = (x - h1[0]) / h1[3]
                t2 = (x - h2[0]) / h2[3]

                if t1 < 0 or t2 < 0: #only interested in the future collision
                    continue

                if mini <= x <= maxi and mini <= y <= maxi: #witihin test area
                    res += 1

    return res//2

print(fx('input24h.txt', 7, 27))
print(fx('input24.txt', 200000000000000, 400000000000000))
