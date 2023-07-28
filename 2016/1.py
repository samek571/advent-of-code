moves = open("input1.txt").read().split(", ")
moves[-1]=moves[-1][:2]

def fx(moves):
    #rotation [n, e, s, w]
    rotation=0
    crocks={0:0, 90:0, 180:0, 270:0}

    for move in moves:
        if move[0]=="R":
            rotation+=90
        else:
            rotation-=90

        rotation%=360
        crocks[rotation]+=int(move[1:])

    print(moves)
    print(crocks)
    return abs(crocks[0]-crocks[180]) + abs(crocks[90]-crocks[270])

print(fx(moves))