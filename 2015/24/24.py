import itertools
import math


def fx(nums, pt2):
    #holdin variable as it would be much slower to compute it within loop everytime
    group_weight = sum(nums) // (3 if not pt2 else 4)

    for n in range(1, len(nums)):
        possibles = [combo for combo in itertools.combinations(nums, n) if sum(combo) == group_weight]
        if possibles:
            return min(math.prod(group) for group in possibles)


print(fx([int(line) for line in open("input24.txt").read().strip().split("\n")], False))
print(fx([int(line) for line in open("input24.txt").read().strip().split("\n")], True))
