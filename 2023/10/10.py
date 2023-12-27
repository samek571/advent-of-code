import collections


def pre(s):
    inp = open(s).read().split('\n')[:-1]

    origin = (-float('inf'), -float('inf'))
    matrix = ['0' * (len(inp[0]) + 2)]
    for idx, line in enumerate(inp):
        matrix.append('0' + line + '0')
        if "S" in line:
            origin = (idx + 1, line.index("S") + 1)
    matrix.append('0' * (len(inp[0]) + 2))


    #finding which 2 dirs are okay to start bfs later
    two_okay = []
    for i,j in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
        dx, dy = origin[0]+i, origin[1]+j

        if 0<=dx<len(matrix) and 0<=dy<=len(matrix[0]):
            if i==-1 and matrix[dx][dy] in {'|', 'F', '7'}:
                two_okay.append(((origin[0], origin[1]), (dx,dy), 0))

            elif i==1 and matrix[dx][dy] in {'|', 'L', 'J'}:
                two_okay.append(((origin[0], origin[1]), (dx,dy), 0))

            elif j==-1 and matrix[dx][dy] in {'-', 'L', 'F'}:
                two_okay.append(((origin[0], origin[1]), (dx,dy), 0))

            elif j==1 and matrix[dx][dy] in {'-', 'J', '7'}:
                two_okay.append(((origin[0], origin[1]), (dx,dy), 0))


    return (two_okay, origin, matrix)



def bfs(s):
    start, origin, matrix = pre(s)

    oracle = {
        'F': [(0,1), (1,0)],
        'L': [(-1,0),  (0,1)],
        '7': [(0,-1), (1,0)],
        'J': [(-1,0),(0,-1)],
        '-': [(0,-1), (0,1)],
        '|': [(-1,0), (1,0)],
    }

    q = start[0]
    perimeter=0
    area = 0
    while True:
        prev, curr, step = q
        if matrix[curr[0]][curr[1]] == "S":
            print('part 1   :',  perimeter//2+1)
            print('part 2   :', -area - perimeter//2)
            return None

        perimeter = max(perimeter, step+1)

        dx, dy = prev[0] - curr[0], prev[1] - curr[1]
        area+= curr[1] * dx #part 2 https://en.wikipedia.org/wiki/Green's_theorem

        to_go = set(oracle[matrix[curr[0]][curr[1]]])
        to_go.remove((dx, dy))
        to_go = list(to_go)

        q = [curr, (curr[0]+to_go[0][0], curr[1]+to_go[0][1]), step+1]


print(bfs('input10.txt'))