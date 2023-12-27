import math
graph = {}
for line in open('input20.txt').read().strip().split('\n'): #doesnt have a testcase...
    parts = line.split(' -> ')
    graph[parts[0]] = parts[1].split(', ')


res = []
for partite in graph['broadcaster']:
    actual = partite
    little_end = ''
    while True:
        g = graph['%'+actual]

        #linked conjs in flipflop result in 1, others in 0; little endian
        little_end = ('1' if len(g) == 2 or '%'+g[0] not in graph else '0') + little_end
        neighs = [neigh for neigh in graph['%'+actual] if '%' + neigh in graph]
        if not neighs: break

        actual = neighs[0]

    res.append(int(little_end, 2))

#i knew immediately it could be a graph of more components and this trick with lcm is trick i used before
#i have seen it on leetcode, learned in freshman year and even used in this very same advent <day10 or so.
print(math.lcm(*res))
print(res)