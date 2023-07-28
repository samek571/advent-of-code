def inputting():
    moves=open("input8.txt").read().split("\n")
    moves.pop()

    return moves

def checker(matrix, x, y):
    ngrs = [[0,1], [0,-1], [1,0], [-1,0]]
    R, C = len(matrix), len(matrix[0])

    for move in ngrs:
        i, j = x+move[0], y+move[1]

        while 0<=i<R and 0<=j<C and int(matrix[x][y]) > int(matrix[i][j]):
            i, j = i+move[0], j+move[1]

        if i in {R,-1} or j in {C, -1}:
            return True

    return False


def fx():
    moves = inputting()
    R, C = len(moves), len(moves[0])
    cnt = 2*(R+C)-4

    for i in moves:
        print(i)
    print("\n")

    for x in range(1, R-1):
        for y in range(1, C-1):
            if checker(moves, x, y):
                print(x,y)
                cnt+=1

    return cnt

print(fx())
# 1662 right one