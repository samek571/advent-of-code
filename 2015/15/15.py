import re
import numpy as np
from functools import reduce


def pre_p(s):
    with open(s) as file:
        lines = file.readlines()
    data = [re.findall("-?\d+", line) for line in lines]
    return [[int(num) for num in line] for line in data]


def _helper(n, limit, curr=[]):
    if len(curr) == n - 1:
        yield curr + [limit - sum(curr)]
    else:
        for i in range(limit - sum(curr) + 1):
            yield from _helper(n, limit, curr + [i])


def fx(data):
    pt1, pt2, combs = 0, 0, list(_helper(len(data), 100))
    for combo in combs:
        tmp = np.dot(np.array(combo), data)

        pt1 = max(pt1, reduce(lambda x, y: x * y, [x if x > 0 else 0 for x in tmp][:-1]))
        if tmp[-1] == 500:
            pt2 = max(pt2, reduce(lambda x, y: x * y, [x if x > 0 else 0 for x in tmp][:-1]))


    return (f"pt1: {pt1}, pt2: {pt2} for {s}")


s = 'input15h.txt'
print(fx(pre_p(s)))
s = 'input15.txt'
print(fx(pre_p(s)))
