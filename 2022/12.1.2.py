from collections import deque

def inputting(s):
    moves=open(s).read().split("\n")
    moves.pop()
    matrix = []
    Epos= [0,0]

    for idx, i in enumerate(moves):
        matrix.append([x for x in i])

        if "E" in i:
            Epos[1] = i.find("E")
            Epos[0] = idx

    return Epos[0], Epos[1], matrix



def bfs(s, p_one):
    ii, jj, matrix = inputting(s)
    s = "a"
    if p_one: s = "S"

    q, visited = deque(), set()
    q.append([ii,jj, 0])
    R, C = len(matrix), len(matrix[0])
    convert = {"S":-1, 'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, "E":26}


    while q:
        x,y,d = q.popleft()

        if (x,y) in visited: continue
        visited.add((x, y))

        print(q)
        for vector in [[0,1], [0,-1], [1,0], [-1,0]]:
            i, j = vector

            if 0<=x+i<R and 0<=y+j<C and convert[matrix[x][y]] <= convert[matrix[x+i][y+j]]+1:
                if matrix[x+i][y+j] == s: return d+1

                q.append([x+i, y+j, d+1])




print(bfs("input12h.txt", p_one=False))
print(bfs("input12h.txt", p_one=True))
#print(bfs("input12.txt", p_one=True))
