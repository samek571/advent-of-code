import collections

def fx(lines):
    res = 0
    for line in lines:
        has_pair = False
        has_repeat = False

        pairs = collections.defaultdict(list)
        for i in range(1, len(line)):
            pair = line[i-1:i+1]
            pairs[pair].append(i-1)
            if len(pairs[pair]) > 1 and pairs[pair][-1] > pairs[pair][-2] + 1:
                has_pair = True

            if i > 1 and line[i] == line[i-2]:
                has_repeat = True

        if has_pair and has_repeat:
            res += 1

    return res


print(fx([line for line in open('input5.txt').read().strip().split("\n")]))