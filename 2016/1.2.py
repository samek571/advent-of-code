moves = open("input1.txt").read().split(", ")
moves[-1]=moves[-1][:2]

def fx(moves):
    encountered={(0,0)}
    rotation = 0
    x=y=0

    for move in moves:
        if move[0]=="R":
            rotation+=90
        else:
            rotation-=90
        rotation%=360


        if rotation==0:
            for _ in range(int(move[1:])):
                y+=1
                if (x,y) in encountered: return abs(x)+abs(y)

                else: encountered.add((x,y))

        if rotation==90:
            for _ in range(int(move[1:])):
                x+=1
                if (x,y) in encountered: return abs(x)+abs(y)

                else: encountered.add((x,y))

        if rotation==180:
            for _ in range(int(move[1:])):
                y-=1
                if (x,y) in encountered: return abs(x)+abs(y)

                else: encountered.add((x,y))

        if rotation==270:
            for _ in range(int(move[1:])):
                x-=1
                if (x,y) in encountered: return abs(x)+abs(y)

                else: encountered.add((x,y))

print(fx(moves))