moves = open("input2.txt").read().split("\n")
moves.pop()

def fx(moves):
    y=0
    x=0

    #matica=[[1],[2,3,4],[5,6,7,8,9],["A","B","C"],["D"]]
    for press in range(len(moves)):

        for move in moves[press]:
            if y==0 and x==-2:
                if move != "R": continue
                else: x+=1

            elif y==0 and x==2:
                if move != "L": continue
                else: x-=1

            elif y==-2 and x==0:
                if move != "U": continue
                else: y+=1

            elif y==2 and x==0:
                if move != "D": continue
                else: y-=1


            elif x==y==1:
                if move == "L": x-=1
                elif move == "D": y-=1
                else:continue

            elif x==y==-1:
                if move == "R": x+=1
                elif move == "U": y+=1

            elif x==-1 and y==1:
                if move == "R": x+=1
                elif move == "D": y-=1

            elif x==1 and y==-1:
                if move == "L": x-=1
                elif move == "U": y+=1


            else:
                if move == "L": x-=1
                elif move == "U": y+=1
                elif move == "R": x+=1
                elif move == "D": y-=1

        print(x,y)
        #print(matica[x+1][y+1])

print(fx(moves))