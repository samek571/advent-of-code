import collections
import math
import re


def pre(s):
    file = open(s).read().split("\n")[:-1]

    instructions, ins_len = file[0], len(file[0])
    graph = collections.defaultdict(tuple)
    for line in file[2:]:
        f = re.findall('[1-9A-Z]+', line)
        graph[f[0]] = (f[1], f[-1])

    res = []
    for line in file[2:]:
        if line[2] == "A":
            i = -1
            step, actual = 0, line[:3]
            while True:
                i = (i+1) % ins_len
                path = 0
                if instructions[i] == "R": path = 1

                step+=1
                actual = graph[actual][path]

                if actual[-1] == "Z": break

            res.append(step)

    return math.lcm(*res)


print(pre('input8.txt'))