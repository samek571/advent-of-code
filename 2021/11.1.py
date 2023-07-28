def parsing():
    moves=open("input11.txt").read().split("\n")
    moves.pop()

    matrix=[]
    for line in moves:
        help=[]
        for char in line:
            help.append(int(char))

        matrix.append(help)

    return matrix


def incrementing(octopuses):
    for lineidx in range(len(octopuses)):
        for charidx in range(len(octopuses[0])):
            octopuses[lineidx][charidx]+=1

    return octopuses
# print(incrementing(parsing()))
def print_o(octopuses):
    for p in octopuses:
        print(p, flush=True)
    print("")

def explode_octupuse_xy(octopuses, x, y, blasts, exploded):
    indexes=[[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
    exploded.add((x, y))
    blasts[0] += 1
    #print(blasts[0])
    print((x,y))
    for i in indexes:
        ix = i[0]
        iy = i[1]
        if x+ix >=0 and x+ix <len(octopuses) and y+iy >=0 and y+iy < len(octopuses[0]) :
            octopuses[x + ix][y + iy] += 1
            if octopuses[x + ix][y + iy] >9 and  (x+ix,y+iy) not in exploded:
                explode_octupuse_xy(octopuses, x+ix, y+iy, blasts,exploded)

def explode_octopuses(octopuses, blasts, exploded):

    for lineidx in range(len(octopuses)):
        for charidx in range(len(octopuses[0])):
            if octopuses[lineidx][charidx] > 9 and (lineidx,charidx) not in exploded:
                explode_octupuse_xy(octopuses,lineidx, charidx, blasts,exploded )




def grounding(octopuses):
    for lineidx in range(len(octopuses)):
        for charidx in range(len(octopuses[0])):
            if octopuses[lineidx][charidx]>9:
                octopuses[lineidx][charidx]=0




def fx():
    octopuses = parsing()
    blasts=[0]
    steps=0
    print_o(octopuses)
    while steps<100:
        exploded=set()
        incrementing(octopuses)
        explode_octopuses(octopuses, blasts,exploded)
        grounding(octopuses)
        print_o(octopuses)
        steps+=1

    return blasts, octopuses

print(fx())
