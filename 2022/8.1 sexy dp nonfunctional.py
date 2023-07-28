def inputting():
    moves=open("input8h.txt").read().split("\n")
    moves.pop()

    up = [int(i) for i in moves[0]]
    down = [int(i) for i in moves[-1]]
    left = [int(moves[i][0]) for i in range(len(moves))]
    right = [int(moves[i][-1]) for i in range(len(moves))]

    print(up, down, left, right)

    return moves, up, down, left, right


def fx():
    moves, up, down, left, right = inputting()
    R, C = len(moves), len(moves[0])
    cnt, seen = 2*(R+C)-4, set()

    for i in moves:
        print(i)
    print("\n")


    for x in range(1, R-1):
        for y in range(1, C-1):

            curr = int(moves[x][y])
            print(up[y], left[x])
            if curr > min(up[y], left[x]):
                cnt+=1
                up[y], left[x] = max(up[y], curr), max(left[x], curr)
                seen.add((x,y))

                print(up[y], left[x])
                print((x,y), curr, "visible\n")

    print("################################")


    for x in range(R - 2, 0, -1):
        for y in range(C - 2, 0, -1):

            curr = int(moves[x][y])
            print(down[y], right[x])
            if (curr > min(down[y], right[x])) and ((x,y) not in seen):
                cnt+=1
                down[y], right[x] = max(down[y], curr), max(right[x], curr)

                print(down[y], right[x])
                print((x,y), curr, "visible\n")


    return cnt

print(fx())
#1828 too high