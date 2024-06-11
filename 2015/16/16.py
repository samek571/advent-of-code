import collections
import re


def pre_p(s):
    return [line for line in open(s).read().strip().split("\n")]


def to_hsh(arr):
    res = [{}]*(len(arr)+1)

    for line in arr:
        hsh = {}
        nums = re.findall("\d+", line)
        words = re.findall("[a-z]+", line)

        idx = int(nums[0])
        for i in range(1, len(words)):
            hsh[words[i]] = int(nums[i])

        res[idx] = hsh

    return res

list_of_all = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

def main(s):
    aunts = to_hsh(pre_p(s))

    for aunt in aunts[1:]: #aunt:dict
        fail_condition = False

        for thing, amount in aunt.items():
            '''pt1'''
        #     if list_of_all[thing] != amount:
        #         break
        # else: return aunts.index(aunt)

            '''pt2'''
            if thing in {"trees", "cats"}:
                if list_of_all[thing] >= amount:
                    fail_condition = True
                    break

            elif thing in {"pomeranians", "goldfish"}:
                if list_of_all[thing] <= amount:
                    fail_condition = True
                    break

            else:
                if list_of_all[thing] != amount:
                    fail_condition = True
                    break


        if not fail_condition:
            return aunts.index(aunt)


print(main("input16.txt"))