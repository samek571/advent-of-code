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
        graph[y].append(x)

    return graph


def fx(s):
    graph = inputting(s)
    queue = collections.deque([("YOU", 0)]); visited = set()

    total = 0
    while queue:
        node, d = queue.popleft()
        if node == "SAN": return d-2

        if node not in visited:
            total+=d
            visited.add(node)

            for adjacent_node in graph[node]:
                queue.append((adjacent_node, d+1))


print(fx("input6.txt"))
#print(fx("input6.txt"))