import collections


def fx(lines):

    res = 0
    for line in lines:

        good_start = False
        bad_string = False
        for i, char in enumerate(line):
            if i==0:
                continue

            conc = line[i-1] + line[i]
            if conc in {"ab","cd","pq","xy"}:
                bad_string = True

            if line[i-1] == line[i]: good_start = True

        dick = collections.Counter(line)
        first_cond = dick["a"] + dick["e"] + dick["i"] + dick["o"] + dick["u"]

        if good_start and first_cond >= 3 and not bad_string:
            res += 1

    return res



print(fx([line for line in open('input5.txt').read().strip().split("\n")]))