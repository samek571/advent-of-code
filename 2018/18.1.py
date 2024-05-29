import collections
import copy


def pre_p(s):
    return [list(line) for line in open(s).read().strip().split("\n")]

def fx(s, time):
    matrix = pre_p(s)
    print(matrix)
    n,m = len(matrix), len(matrix[0])
    tmp_matrix = copy.deepcopy(matrix)

    neigh = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    relations = [".", "|", "#"]

    minute = 0
    cache = {}
    state_list = []

    while minute < time:
        
        #cache for part 2
        state_tuple = tuple(tuple(row) for row in matrix) #cant store list in hashmap
        if state_tuple in cache:
            retrieve_time = cache[state_tuple]
            remaining_minutes = (time - minute) % (minute - retrieve_time)
            matrix = [list(row) for row in state_list[retrieve_time + remaining_minutes]]
            break

        cache[state_tuple] = minute
        state_list.append(state_tuple)
        
        for x in range(n):
            for y in range(m):

                #seeing neighbors
                dick = collections.defaultdict(int)
                for xi,yj in neigh:
                    i,j = x+xi, y+yj

                    if (0<=i<n and 0<=j<m):
                        dick[matrix[i][j]] += 1

                #might change $leq + it can be done hella nicer
                if matrix[x][y] == relations[0]:
                    if dick[relations[1]]>=3:
                        tmp_matrix[x][y] = relations[1]
                    else:
                        tmp_matrix[x][y] = relations[0]

                elif matrix[x][y] == relations[1]:
                    if dick[relations[2]]>=3:
                        tmp_matrix[x][y] = relations[2]
                    else:
                        tmp_matrix[x][y] = relations[1]

                elif matrix[x][y] == relations[2]:
                    if dick[relations[2]]>=1 and dick[relations[1]]>=1:
                        tmp_matrix[x][y] = relations[2]
                    else:
                        tmp_matrix[x][y] = relations[0]

        matrix = copy.deepcopy(tmp_matrix)
        minute+=1

    return sum(row.count('|') for row in matrix) * sum(row.count('#') for row in matrix)





print(fx('input18h.txt', 10))
print(fx('input18.txt', 10))
print(fx('input18.txt', 1000000000))