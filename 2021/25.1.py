import copy


def inputting():
    moves=open("input25.txt").read().split("\n")
    moves.pop()
    matrix = []

    for i in moves:
        help=[]
        for char in i:
            help.append(char)

        matrix.append(help)

    return matrix
#print(inputting())



def fx():
  sea = inputting()
  counter = 0
  horl = len(sea)
  vertl = len(sea[0])

  while True:
    counter+=1
    moved = False
    sea2 = copy.deepcopy(sea)

    #eastfacing
    for lineidx in range(horl):
        for charidx in range(vertl):
            if sea[lineidx][charidx] == ">":
                if sea[lineidx][(charidx+1)%vertl] == ".":
                    moved=True
                    sea2[lineidx][charidx] = "."
                    sea2[lineidx][(charidx+1)%vertl] = ">"

    sea3 = copy.deepcopy(sea2)


    #south
    for lineidx in range(horl):
        for charidx in range(vertl):
            if sea2[lineidx][charidx] == "v":
                if sea2[(lineidx + 1) % horl][charidx] == ".":
                    moved=True
                    sea3[lineidx][charidx] = "."
                    sea3[(lineidx + 1) % horl][charidx] = "v"

    for i in sea3:
        print(''.join(i))
    print("\n^^_new_^^, vv_old_vv\n")
    for i in sea:
        print(''.join(i))
    print("\n", counter)
    print("########################################################################\n")


    if not moved: return counter
    sea=sea3

print(fx())
