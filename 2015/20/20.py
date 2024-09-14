def fx(target, pt2):
    res = 1
    while True:
        if not pt2:
            sm = 10 * sum(d for d in range(1, int(res ** 0.5) + 1) if res % d == 0 for d in {d, res // d})
        else:
            sm = 11 * sum(d for d in range(1, int(res ** 0.5) + 1) if res % d == 0 for d in {d, res // d} if res // d <= 50)

        if sm >= target: return res
        res += 1

#takes like 15sec per run
print(fx(33100000, False))
print(fx(33100000, True))
