import re
from re import compile
from operator import mul, itemgetter
from functools import reduce
from itertools import tee, filterfalse, chain

global_value = compile('value (\d+) goes to (bot \d+)')
global_bot = compile('(bot \d+) gives low to ((?:output|bot) \d+) and high to ((?:output|bot) \d+)')

def pre_p(lines, regex):
    result = []
    for line in lines:
        match = regex.match(line)
        if match:
            result.append(match.groups())
    return result

def partition(pred, iterable): #little deeper knowledge of python
    t1, t2 = tee(iterable)
    return filterfalse(pred, t1), filter(pred, t2)

def _bot(low, high, bins):
    def dist_a(a):
        def dist_b(b):
            h, l = max(a, b), min(a, b)
            bins[high] = bins[high](h)
            bins[low] = bins[low](l)
            return (h, l)
        return dist_b
    return dist_a

def _eval(inputs, cmds, bins):
    for bot, low, high in cmds:
        bins[bot] = _bot(low, high, bins)

    for val, bot in inputs:
        bins[bot] = bins[bot](int(val))

def f(bins):
    tmp = ((int(k.split(" ")[-1]), v) for k, v in bins.items() if k.startswith("output"))
    return [v for k, v in sorted(tmp, key=itemgetter(0))]

def main(input):
    inputs, cmds = partition(lambda s: s.startswith("bot"), input)
    inputs, cmds = pre_p(inputs, global_value), pre_p(cmds, global_bot)

    bins = {x:lambda y: y for x in chain.from_iterable(cmds)}
    _eval(inputs, cmds, bins)

    outputs = f(bins)
    return {v:k for k, v in bins.items()}[(61, 17)], reduce(mul, outputs[:3], 1)

input = [x.strip() for x in open("input10.txt").read().split("\n")]
print(main(input))