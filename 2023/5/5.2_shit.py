from intervaltree import IntervalTree
import re
def preprocess(s):

    inp = open(s).read().split("\n")[:-1]
    seeds = list(map(int, re.findall('[0-9]+', inp[0])))

    translations = []
    converter = []
    for line in inp[2:]:
        if not line:
            a = sorted(converter, key=lambda x: x[1])
            translations.append(a)
            converter = []
        elif "-" in line:
            continue
        else:
            converter.append(list(map(int, re.findall('[0-9]+', line))))
    translations.append(converter)

    return seeds, translations


def create_interval_tree(mapping):
    tree = IntervalTree()
    for end, start, range_size in mapping:
        tree[start:start+range_size] = end - start

    return tree

# def alamnac_zora(seed, trees):
#     for tree in trees:
#         intervals = tree[seed]
#         for interval in intervals:
#             seed += interval.data
#
#     return seed

def alamnac_zora(interval, trees):
    start, end = interval
    min_value = float('inf')
    for value in range(start, end):
        transformed_value = value
        for tree in trees:
            intervals = tree[transformed_value]
            for interval in intervals:
                transformed_value += interval.data
        min_value = min(min_value, transformed_value)
    return min_value


def fx(s):
    seeds, translations = preprocess(s)
    minimum = float('inf')
    trees = [create_interval_tree(obj) for obj in translations]

    for idx in range(1, len(seeds), 2):
        interval = (seeds[idx-1], seeds[idx-1] + seeds[idx])
        minimum = min(alamnac_zora(interval, trees), minimum)

    return minimum

print(fx('input5.txt'))
