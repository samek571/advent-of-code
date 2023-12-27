import collections
import re


def pre(s):
    file = open(s).read().split("\n")[:-1]

    instructions, ins_len = file[0], len(file[0])
    graph = collections.defaultdict(tuple)
    for line in file[2:]:
        f = re.findall('[A-Z]+', line)
        graph[f[0]] = (f[1], f[-1])

    i = -1
    step, actual = 0, "AAA"
    while True:
        i = (i+1) % ins_len
        path = 0
        if instructions[i] == "R": path = 1

        step+=1
        actual = graph[actual][path]

        if actual == 'ZZZ': return step



print(pre('input8.txt'))