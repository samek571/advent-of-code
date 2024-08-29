def fx(directions):
    santa = (0, 0)
    robo = (0, 0)
    seen = set()
    seen.add((0, 0))

    move_map = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}

    for i, d in enumerate(directions):
        if i % 2 == 0:
            santa = (santa[0] + move_map[d][0], santa[1] + move_map[d][1])
            seen.add(santa)
        else:
            robo = (robo[0] + move_map[d][0], robo[1] + move_map[d][1])
            seen.add(robo)

    return len(seen)

print(fx("".join([line for line in open('input3.txt').read().strip().split("\n")])))
