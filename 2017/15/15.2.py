def gen(v, f):
    return (v * f) % (2 ** 31 - 1)


def fx(a, b, num):
    fa, fb = 16807, 48271
    ca, cb = 4,8

    res = 0
    match_count = 0
    while match_count < num:
        a = gen(a, fa)
        while a % ca != 0:
            a = gen(a, fa)

        b = gen(b, fb)
        while b % cb != 0:
            b = gen(b, fb)

        if (a & 0xFFFF) == (b & 0xFFFF):
            res += 1

        match_count += 1

    return res


print(fx(591, 393, 5 * 10 ** 6))  # A star and B start
# print(fx(65, 8921, 40*10**6)) #testcase