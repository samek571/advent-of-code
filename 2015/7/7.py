def pre_p(lines):
    ins = {}
    for line in lines:
        p = line.strip().split(' -> ')
        expr, f = p[0], p[1]
        ins[f] = expr

    return ins


def fx(wire, ins, values):
    if wire.isdigit(): return int(wire)
    if wire in values: return values[wire]

    expr = ins[wire]
    p = expr.split()

    if len(p) == 1:
        res = fx(p[0], ins, values)

    elif len(p) == 2:
        operand = fx(p[1], ins, values)
        res = ~operand & 0xFFFF

    elif len(p) == 3:
        left = fx(p[0], ins, values)
        op = p[1]
        right = fx(p[2], ins, values)

        if op == 'AND':
            res = left & right
        elif op == 'OR':
            res = left | right
        elif op == 'LSHIFT':
            res = (left << int(p[2])) & 0xFFFF
        elif op == 'RSHIFT':
            res = (left >> int(p[2])) & 0xFFFF

    values[wire] = res
    return res


'''pt1'''
ins = pre_p([line for line in open('input7.txt').read().strip().split("\n")])
pt1 = fx('a', ins, {})
print(pt1)


'''part2'''
ins['b'] = str(pt1)
pt2 = fx('a', ins, {})
print(pt2)