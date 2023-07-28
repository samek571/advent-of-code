import copy

def inputting():
    moves=open("input20.txt").read().split("\n")
    moves.pop()
    matrix=[]
    for i in moves[2:]:
        temp=[]
        for char in i:
            temp.append(char)
        matrix.append(temp)

    return moves[0], matrix
#print(inputting())


def extend(i, grid,default):
    new =[]
    for _ in range(i):
        new.append([default] * (i+len(grid[0])+i))

    for lineidx in range(len(grid)):
        help=[]
        for _ in range(i):
            help.append(default)

        for o in grid[lineidx]:
            help.append(o)

        for _ in range(i):
            help.append(default)

        new.append(help)

    for _ in range(i):
        new.append([default] * (i+len(grid[0])+i))

    return new
#import pprint
#pp= pprint.PrettyPrinter(width=120, compact=True)
#pprint.pprint( [['#', '.', '.', '#', '.'], ['#', '.', '.', '.', '.'], ['#', '#', '.', '.', '#'], ['.', '.', '#', '.', '.'], ['.', '.', '#', '#', '#']])
#pp.pprint( extend(2,extend(2, [['#', '.', '.', '#', '.'], ['#', '.', '.', '.', '.'], ['#', '#', '.', '.', '#'], ['.', '.', '#', '.', '.'], ['.', '.', '#', '#', '#']])))


def count(grid):
    output=0
    for line in range(len(grid)):
        for char in range(len(grid[0])):
            if grid[line][char] == "#": output+=1

    return output
#print(counter([['#', '.', '.', '#', '.'], ['#', '.', '.', '.', '.'], ['#', '#', '.', '.', '#'], ['.', '.', '#', '.', '.'], ['.', '.', '#', '#', '#']]))


def getg(grid,x,y,i,j,default):
        if len(grid)<=x+i or x+i<0:
                return default
        if len(grid[0])<=y+j or y+j<0:
                return default
        return grid[x+i][y+j]

def printg(grid):
    for l in grid:
        print("".join(l))

def main(number_of_iterations):
    iea, grid = inputting()

#    print('input:')
#    printg(grid)
#    print('end input')

    default='.'
    flip=dict()
    if iea[0] =='.':
        flip['.']='.'
    else:
        if iea[511]=='.':
            flip['.']='#'
            flip['#']='.'
        else:
            return 'infinity'

    for iteration in range(number_of_iterations):
        grid = extend(1, grid,default)
#        print(iteration,"after extend, before flip")
#        printg(grid)
        new=copy.deepcopy(grid)
        for lineidx in range(len(grid)):
            for charidx in range(len(grid[0])):

                to_binary=''
                for i in range(-1,1+1):
                    for j in range(-1,1+1):
                        if getg(grid,lineidx,charidx,i,j,default) == ".":
                                to_binary+="0"
                        else:
                                to_binary+="1"

                iea_idx = int(to_binary, 2)
                new[lineidx][charidx] = iea[iea_idx]
        default=flip[default]

        grid = new
#        print(iteration,"after flip")
#        printg(grid)
#        print("")
#        print(count(new))

    return count(grid)

print(main(2))
print(main(50))

#5367 too low
#5578 too high
#5647 too high and right answer for someone else XD?
