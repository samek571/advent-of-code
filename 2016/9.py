def fx(garbage):
    p, res = 0, 0
    while p < len(garbage):
        if garbage[p] == '(':
            end_p = garbage.index(')', p)
            tmp = garbage[p+1 : end_p]
            chars, repeat = map(int, tmp.split('x'))
            p = end_p + 1
            p, res = p+chars, res + chars*repeat
        else:
            p, res = p+1, res+1

    return res

#s='input9.txt'
#print(fx(*[line for line in open(s).read().strip().split("\n")]))


import re
def fx2(garbage):
    bracket = re.search(r'\((\d+)x(\d+)\)', garbage)
    if not bracket: return len(garbage)
    
    pos = bracket.start(0)
    size, repeat = int(bracket.group(1)), int(bracket.group(2))
    p = pos + len(bracket.group())

    return len(garbage[:pos]) + fx2(garbage[p:p + size]) * repeat + fx2(garbage[p + size:])


s='input9.txt'
print(fx2(*[line for line in open(s).read().strip().split("\n")]))

#735684 too low