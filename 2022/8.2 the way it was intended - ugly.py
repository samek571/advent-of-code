import math

def inputting():
    moves=open("input8.txt").read().split("\n")
    moves.pop()
    return moves


def checker(matrix, x, y):
    ngrs, R, C, scenic = [[-1,0], [0,-1], [0,1], [1,0]], len(matrix), len(matrix[0]), []

    for move in ngrs:
        i, j = x+move[0], y+move[1]

        cnt = 1
        while 0<i<R-1 and 0<j<C-1 and int(matrix[x][y]) > int(matrix[i][j]):
            cnt+=1

            i, j = i+move[0], j+move[1]

        scenic.append(cnt)


    return math.prod(scenic)

# print(checker(inputting(), 1, 2))
# print(checker(inputting(), 3, 2))


def fx():
    moves = inputting()
    R, C = len(moves), len(moves[0])
    cnt = 0

    for i in moves:
        print(i)
    print("\n")

    for x in range(1, R-1):
        for y in range(1, C-1):
             cnt = max(cnt, checker(moves, x, y))

    return cnt

print(fx())
