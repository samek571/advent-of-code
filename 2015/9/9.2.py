import collections

#the backbone
def dfs(curr_city, seen, path, curr_dist):
    global res, best_path
    if len(seen) == len(dist):
        if curr_dist > res: #part2
            res = curr_dist
            best_path = path[:]
        return

    for next_city in range(len(dist)):
        if next_city not in seen:
            seen.add(next_city)
            path.append(next_city)
            dfs(next_city, seen, path, curr_dist + dist[curr_city][next_city])
            seen.remove(next_city)
            path.pop()


# Parsing
#'London': {'Dublin': 464, 'Belfast': 518},
dick = collections.defaultdict(dict)
s = 'input9.txt'
tmp = [line for line in open(s).read().strip().split("\n")]
for line in tmp:
    line = line.split()
    dick[line[0]][line[2]] = int(line[-1])
    dick[line[2]][line[0]] = int(line[-1])

cities = list(dick.keys())
dist = [[0] * len(cities) for _ in cities]

for i, city in enumerate(cities):
    for j, dest in enumerate(cities):
        if city == dest:
            dist[i][j] = 0
        else:
            dist[i][j] = dick[city][dest]


#run
res = -float('inf') #part2
best_path = []

for start_city in range(len(cities)):
    dfs(start_city, {start_city}, [start_city], 0)

print(res)