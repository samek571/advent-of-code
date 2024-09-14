def fx(ins, pt2):
    reg = {'a': 0, 'b': 0}
    if pt2: reg["a"] = 1

    p = 0
    while 0 <= p < len(ins):
        pts = ins[p].split()

        if pts[0] == 'hlf':
            reg[pts[1]] //= 2
            p += 1
        elif pts[0] == 'tpl':
            reg[pts[1]] *= 3
            p += 1
        elif pts[0] == 'inc':
            reg[pts[1]] += 1
            p += 1
        elif pts[0] == 'jmp':
            offset = int(pts[1])
            p += offset
        elif pts[0] == 'jie':
            register = pts[1].strip(',')
            offset = int(pts[2])
            if reg[register] % 2 == 0:
                p += offset
            else:
                p += 1
        elif pts[0] == 'jio':
            register = pts[1].strip(',')
            offset = int(pts[2])
            if reg[register] == 1:
                p += offset
            else:
                p += 1

    return reg['b']


ins = [line for line in open('input23.txt').read().strip().split("\n")]
print(fx(ins, pt2=False))
print(fx(ins, pt2=True))
