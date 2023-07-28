import collections

def inputting(s):
    matrix=open(s).read().split("\n")
    matrix.pop()

    graph = collections.defaultdict(list)
    for line in matrix:
        line = line.split(")")
        print(line)
        x,y = line[0], line[1]
        graph[x].append(y)

    return graph

#coulda be done with dfs aswell, no need for dq
def fx(s):
    graph = inputting(s)
    queue = collections.deque([("COM", 0)])

    total = 0
    while queue:
        node, d = queue.popleft()
        total+=d

        for adjacent_node in graph[node]:
            queue.append((adjacent_node, d+1))

    return total

print(fx("input6.txt"))
#print(fx("input6h.txt"))