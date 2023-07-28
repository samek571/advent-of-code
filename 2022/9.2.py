'''
ITs NOT THIS
now its the same shit as before just rope is longer --> we only care about the last one which is
9 apart from head, meaning if it gets 10 tiles apart, tail moves the closest to the actual head

ITS THIS
same as the part 1 just each 1-9 tail is dependant on the previous one --> its important that if the head moves and 1 gets
longer distance than 1 in x|y axis - we make xdif and ydif and move 1 the best direction possible towards the Head.
Now same shit for the 2 and 1; with 2 being 1 and 1 being Head. Same for 32 43 54 65 76 87 98



- set of visited by tail
- iterates via all the udlr instructions and
    --marks head pos, if abs(xyhead - xytail) is more than 10: tail gets prev head pos

'''

def inputting():
    moves=open("input9.txt").read().split("\n")
    moves.pop()
    return moves


def fxmain(lenght):
    tails = [(0,0) for _ in range(lenght+1)]
    seen, leads = {tails[0]}, {"R":(0,1), "L":(0,-1), "U":(-1, 0), "D":(1,0)}


    for instruction in inputting():
        print(instruction)

        vector = leads[instruction[0]]
        for number_of_moves in range(int(instruction[2:])):
            #head moves as its told
            tails[0] = (tails[0][0] + vector[0], tails[0][1] + vector[1])

            #check whether all tails satisfy being at max +-1 in any direction --> delta x or delta y > 1 is bad
            # and requires immediate reparation by moving particular tail towards his neighbor by the best vector
            # which is determined by

            for idx in range(1, lenght+1):

                #Hx-1x or Hy-1y
                xdif, ydif = tails[idx-1][0] - tails[idx][0], tails[idx-1][1] - tails[idx][1]
                if abs(xdif)>1 or abs(ydif)>1:
                    x, y = xdif, ydif

                    if xdif >1: x=1
                    if xdif<-1: x=-1
                    if ydif >1: y=1
                    if ydif<-1: y=-1

                    tails[idx] = (tails[idx][0] + x, tails[idx][1] + y)

            seen.add(tails[-1])

            print(tails)


    return len(seen)

#print(fxmain(1))
print(fxmain(9))
# 410 too low
# 3865 too high


"""
def fxmain(lenght):
    x,y = 0, 0
    tail, seen = (x,y), {(x,y)}
    leads = {"R":(0,1), "L":(0,-1), "U":(-1, 0), "D":(1,0)}

    for instruction in inputting():
        print(instruction)


        vector = leads[instruction[0]]
        for number_of_moves in range(int(instruction[2:])):

            #head moves as its told and we check if tail isnt too far and away
            x, y = x + vector[0], y + vector[1]
            xdif, ydif = x-tail[0], y-tail[1]
            if abs(xdif)>lenght or abs(ydif)>lenght:
                # if it is, tail makes the closest move towards the head moving only 1 tile
                if xdif > 0: xdif=1
                elif xdif <0: xdif=-1
                if ydif > 0: ydif=1
                elif ydif <0: ydif=-1

                tail = (tail[0]+xdif, tail[1]+ydif)
                seen.add(tail)


    return len(seen)

"""