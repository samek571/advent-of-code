from heapdict import heapdict
import pprint

f=open("21-15-1.txt")
M = [[int(x) for x in s.strip()] for s in f.readlines()]

def expand5(M):
    top = []
    for row in M:
        temp = []
        for i in range(0,5):
            temp += [(x +i) % 9  if (x +i) % 9 !=0 else 9 for x in row]
        top.append(temp)
    ret = top.copy()
    for i in range(1, 5):
        for row in top:
           ret.append([(x+i) % 9 if (x+i) % 9 !=0 else 9 for x in row])
    return ret

def f():
        NEIGHBORS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        rows = len(M)
        columns = len(M[0])
        INF=99999999999999
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

                if ((0 <= neigh[0] < rows) and ( 0 <= neigh[1] < columns)  and neigh not in visited):

                        tmp = result[node[0]][node[1]] + M[neigh[0]][neigh[1]]
                        
                        if tmp < result[neigh[0]][neigh[1]] or \
                            result[neigh[0]][neigh[1]] == INF:

                            result[neigh[0]][neigh[1]] = tmp
                            Q[neigh] = tmp


        return result[-1][-1]

print( f() )
M=expand5(M)
#for x in M:
#    print("".join([str(i) for i in x]))

print( f() )

