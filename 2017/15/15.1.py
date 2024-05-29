def gen(v, f):
    return (v * f) % (2**31-1)


def fx(a,b,num):
    fa, fb = 16807, 48271

    res = 0
    for _ in range(num):
        a = gen(a, fa)
        b = gen(b, fb)
    
        if (a & 0xFFFF) == (b & 0xFFFF):
            res += 1
    
    return res


print(fx(591, 393, 40*10**6)) #A star and B start
#print(fx(65, 8921, 40*10**6)) #testcase