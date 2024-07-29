import re


def pre_p(s):
    return [line for line in open(s).read().strip().split("\n")]

def fx(data):
    res1, res2 = 0, 0
    for case in data:
        # #p = r'\\x..|\\\\|\\"'
        # p = r'\\x[0-9A-Fa-f]{2}|\\\\(?!x[0-9A-Fa-f]{2})|\\"'
        # filtered = re.findall(p, case)
        # print(filtered)
        print(case)

        f1 = len(re.findall("\\\[\"\\\]", case))
        f2 = 3*len(re.findall("\\\[x][0-9A-Fa-f]{2}", case))
        print(f2, f1)
        res1+=f2+f1+2

        f1 = 2*len(re.findall("\\\[\"\\\]", case))
        f2 = len(re.findall("\\\[x][0-9A-Fa-f]{2}", case))
        res2+=f2+f1+4

    return res1, res2

# fx(["cyxdpkh\\\""])
# fx(["kwdlysf\\xjpelae"])
# fx(["\"\"r"])
# fx(["nsvcquyxbwilsxxemf\xd9leq"])

print(fx(pre_p('input8.txt')))
