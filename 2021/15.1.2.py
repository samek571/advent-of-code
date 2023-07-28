
def parsing():
    moves=open("input15.txt").read().split("\n")
    moves.pop()

    matrix=[]
    for line in moves:
        help=[]
        for char in line:
            help.append(int(char))

        matrix.append(help)

    for i in matrix:
        print(i)

    return matrix
print(parsing())

def expansion():
    matrix = parsing()
    biggermatrix=[]
    for line in matrix:
        temp=[]
        temp+=line
        for i in range(1, 5):
            for char in line:
                if char+i>=10: char-=9
                temp.append(char+i)

        biggermatrix.append(temp)
    for i in biggermatrix:
        print(i)

    print("")


    massivematrix=[]
    massivematrix+=biggermatrix
    for i in range(1,5):

        for line in biggermatrix:
            temppppp=[]
            for char in line:
                if char+i>=10: char-=9
                temppppp.append(char+i)

            massivematrix.append(temppppp)

    for u in massivematrix:
        print(u)

    return massivematrix
print(expansion())

def f():
    NEIGHBORS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    M=parsing()
    rows = len(M)
    columns = len(M[0])
    INF = 99999999999999
    result = [[INF for _ in range(rows)] for _ in range(columns)]
    result[0][0] = 0
    Q = heapdict()
    Q[(0, 0)] = 0
    visited = set()

    while Q:
        node, dist = Q.popitem()
        visited.add(node)

        for n in NEIGHBORS:
            neigh = (node[0] + n[0], node[1] + n[1])

            if ((0 <= neigh[0] < rows) and (0 <= neigh[1] < columns) and neigh not in visited):

                tmp = result[node[0]][node[1]] + M[neigh[0]][neigh[1]]

                if tmp < result[neigh[0]][neigh[1]] or \
                        result[neigh[0]][neigh[1]] == INF:
                    result[neigh[0]][neigh[1]] = tmp
                    Q[neigh] = tmp

    return result[-1][-1]

print( f() )