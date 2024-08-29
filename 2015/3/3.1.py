def fx(directions):
    x, y = 0, 0
    seen = set()
    seen.add((x, y))

    for d in directions:

        if d == '^': y += 1
        elif d == 'v': y -= 1
        elif d == '>': x += 1
        elif d == '<': x -= 1

        seen.add((x, y))

    return len(seen)

print(fx("".join([line for line in open('input3.txt').read().strip().split("\n")])))
