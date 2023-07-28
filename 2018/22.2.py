from heapq import heappush, heappop

with open('input22.txt', 'r') as f:
    depth = int(next(f).split()[-1])
    target = complex(*map(int, next(f).split()[-1].split(',')))


ROCKY, WET, NARROW = 0, 1, 2
NEITHER, TORCH, CLIMB = 0, 1, 2
m_erosion = dict()
m_geo_index = dict()


def viz(max):
    m_viz_erosion = {ROCKY: '.', WET: '=', NARROW: '|'}

    for y in range(int(max.imag) + 1):
        for x in range(int(max.real) + 1):
            pos = x + 1j * y
            if pos == 0:
                print('M', end='')
            elif pos == target:
                print('T', end='')
            else:
                print(m_viz_erosion[erosion(pos) % 3], end='')
        print()


# holding all positions (in a complex numbers - avoiding unnecessary grid traversals) in a dictionary (O(1) search)
def erosion(pos):
    if pos in m_erosion:
        return m_erosion[pos]

    new_val = (geo_index(pos) + depth) % 20183
    m_erosion[pos] = new_val
    return new_val

# computing if we are out of the boundaries
def geo_index(pos):
    if pos in m_geo_index:
        return m_geo_index[pos]

    if pos == 0 or pos == target:
        new_val = 0
    elif pos.imag == 0:
        new_val = pos.real * 16807
    elif pos.real == 0:
        new_val = pos.imag * 48271
    else:
        new_val = erosion(pos - 1) * erosion(pos - 1j)

    m_geo_index[pos] = new_val
    return new_val


# Part 1
# risk = 0
# for y in range(int(target.imag) + 1):
#     for x in range(int(target.real) + 1):
#         risk += erosion(x + 1j * y) % 3
# print('Part 1:', int(risk))


# Part 2
# Do a BFS search with a priority queue.
heap = [(0, 0, 0, TORCH)]  # (time, x, y, equipment), heap sorted by time, so time has to be first
visited = {(0, TORCH): 0}  # (pos, equipment): time

def visit_next(time, pos, eqp, heap):
    for newpos in [pos + 1, pos - 1, pos + 1j, pos - 1j]:
        if newpos.real < 0 or newpos.imag < 0:                         # out of bounds
            continue
        if erosion(newpos) % 3 == eqp:                                  # reachable with this equipment
            continue
        if (newpos, eqp) in visited and visited[(newpos, eqp)] <= time:  # there is a faster way
            continue
        visited[(newpos, eqp)] = time                                   # mark the faster time
        heappush(heap, (time, newpos.real, newpos.imag, eqp))           # put neighbor to heap


while True:
    # It's annoying we cannot use the heap with complex numbers because they cannot be ordered...
    time, x, y, eqp = heappop(heap)
    pos = x + 1j * y
    if (pos, eqp) == (target, TORCH):
        break

    # Try to go to the next square with the same equipment
    time += 1
    visit_next(time, pos, eqp, heap)

    # Try to go to the next square with alternative equipment
    # The region's type and the two allowed equipments always sum to 3, no need to do an additional hashmap
    time += 7
    eqp = 3 - eqp - erosion(pos) % 3
    visit_next(time, pos, eqp, heap)

print('Part 2:', time)







"""
import copy
from collections import deque

def pre(depth, x,y, e):
    x, y= 1+x, 1+y
    matrix = [[0]*(x+e) for _ in range(y+e)]
    mod, matrix[0][0] =  20183, depth

    #erosion level at 0,y and x,0
    for line_idx in range(1, y+e): matrix[line_idx][0] = (depth + line_idx*48271)%mod
    for char_idx in range(1, x+e): matrix[0][char_idx] = (depth + char_idx*16807)%mod

    '''erosion level completed'''
    for line_idx in range(1, y+e):
        for char_idx in range(1, x+e):
            if not(y-1==line_idx) or not(x-1==char_idx):
                matrix[line_idx][char_idx] = (depth + matrix[line_idx][char_idx-1] * matrix[line_idx-1][char_idx])%mod
            else:
                matrix[y - 1][x - 1] = depth


    '''matrix mod3'''
    #total = 0
    for line_idx in range(y+e):
        for char_idx in range(x+e):
            matrix[line_idx][char_idx] = matrix[line_idx][char_idx]%3
        # if line_idx < y:
        #     total += sum(matrix[line_idx][:-e])

    '''drawn'''
    picogram = copy.deepcopy(matrix)
    trans = {0: ".", 1: "=", 2: "|"}
    for line_idx in range(y+e):
        for char_idx in range(x+e):
            if line_idx == y-1 and char_idx == x-1:
                picogram[line_idx][char_idx] = "T"
            else:
                picogram[line_idx][char_idx] = trans[matrix[line_idx][char_idx] % 3]
        print("".join(picogram[line_idx]))


    return matrix



def bfs(depth, x, y, e):
    M = pre(depth, x, y, e)
    NEIGHBORS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    C = len(M[0])+e
    R = len(M)+e
    INF = float('inf')

    result_matrix = [[INF for _ in range(R)] for _ in range(C)]
    result_matrix[0][0] = 0
    Q = deque([[0,0]])
    visited = set()

    for i in result_matrix:
        print(i)
    print(len(result_matrix), len(result_matrix[0]))

    for i in M:
        print(i)
    print(len(M), len(M[0]))

    while Q:
        node = Q.popleft()
        visited.add(str(node))

        #4 neighbors
        for n in NEIGHBORS:
            neigh = (node[0] + n[0], node[1] + n[1])

            #in grid and not seen
            if ((0 <= neigh[0] < R) and (0 <= neigh[1] < C) and str(neigh) not in visited):
                tmp = result_matrix[node[0]][node[1]] + M[neigh[0]][neigh[1]]

                if tmp < result_matrix[neigh[0]][neigh[1]] or result_matrix[neigh[0]][neigh[1]] == INF:
                    result_matrix[neigh[0]][neigh[1]] = tmp
                    Q.append([neigh[0], neigh[1]])

    return result_matrix[x-1][y-1]


#print(pre(510, 10, 10, 5))
#print(pre(7740, 12, 763))

print(bfs(510, 10, 10, 5))




# append {3neighbor locations, 3 changes of env that happened, lvl} to dequeue
# make a matrix thats stores the least time it took to own every cell 
# 
# bfs / dijkstra




    # for i in range(1, y+e): matrix[0][i] += matrix[0][i - 1]
    # for i in range(1, x+e): matrix[i][0] += matrix[i - 1][0]
    #
    # for i in range(1, x+e):
    #     for j in range(1, y+e):
    #         matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])
    #     print(matrix[i])
    #
    # return matrix[x-1][y-1]


"""