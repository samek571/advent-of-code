import collections

def part2(s):
    matrix = [[i for i in line] for line in open(s).read().strip().split("\n")]
    h = len(matrix) ; w = len(matrix[0])
    results = []
    for x in range(h):
        for y in range(w):
            if x not in [0, h - 1] and y not in [0, w - 1]:
                continue

            for d in range(4):
                results.append(bfs(matrix, (y, x), d))

    return max(results)


def bfs(matrix, start, d):
    h = len(matrix) ; w = len(matrix[0])
    odd_oraculum = {'|':[-1, 1], '-':[0], '\\':[1], '/':[-1], '.':[0]}
    even_oraculum = {'|':[0], '-':[-1,1], '\\':[-1], '/':[1], '.':[0]}
    dirs = [(-1,0), (0,1), (1,0), (0,-1)] #n e s w
    seen = set() #set for each location IN EACH DIRECTION to prevent loops

    q = collections.deque([(start, d)]) #init
    while q:
        pos, d = q.popleft()

        if (pos, d) in seen: continue
        seen.add((pos, d))

        curr = matrix[pos[0]][pos[1]]
        next_dirs = [(d+e)%4 for e in (odd_oraculum[curr] if d % 2 == 1 else even_oraculum[curr])]

        for dir in next_dirs:
            new_d = dirs[dir]
            x,y = pos[0]+new_d[0], pos[1]+new_d[1]
            if 0 <= x < h and 0 <= y < w and ((x, y), new_d) not in seen:
                q.append(((x, y), dir))

    return len(set(pos for pos, _ in seen))

print(part2('input16.txt'))