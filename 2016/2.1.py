moves = open("input2.txt").read().split("\n")
moves.pop()

def fx(moves):
    outpur=""
    print(moves)
    x=y=0

    matica=[[1,2,3],[4,5,6],[7,8,9]]

    for press in range(len(moves)):

        for move in moves[press]:
            if move == "R":
                if x!=1:
                    x+=1

            elif move == "L":
                if x!=-1:
                    x-=1

            elif move == "U":
                if y!=1:
                    y +=1

            else:
                if y!=-1:
                    y-=1

        print(x,y)
        #print(matica[x+1][y+1])

print(fx(moves))
#74985