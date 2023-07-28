VERSIONS=[]
def initializationen():
    return ''.join(format(int(x, 16), '04b') for x in open('input16.txt', 'r').read().strip())

print(initializationen())

def parse_literal(s, idx):
    res = []
    while s[idx] == '1':
        res.append(s[idx + 1 : idx + 5])
        idx += 5
    res.append(s[idx + 1 : idx + 5])
    idx += 5
    return idx, int(''.join(res), 2)


def parse_packet(s, idx):
    print(idx, s)
    version, T = int(s[idx : idx + 3], 2), int(s[idx + 3 : idx + 6], 2)
    VERSIONS.append(version)
    if T == 4:
        new_idx, val = parse_literal(s, idx + 6)
        return new_idx, val

    # else vetva -- operator

    idx+=6

    values = []
    I = s[idx]
    idx+=1
    val = 0
    if I == '0':
        total_len = int(s[idx : idx + 15], 2)
        idx += 15
        old_idx=idx
        while idx < old_idx + total_len:
            idx, val = parse_packet(s, idx)
            values.append(val)
    else:  # I == '1'
        packets = int(s[idx : idx + 11], 2)
        idx += 11
        for _ in range(packets):
            idx, val = parse_packet(s, idx)
            values.append(val)


    if T == 0:
        return idx,sum(values)

    elif T == 1:
        val = 1
        for k in values:
            val *= k

        return idx, val

    elif T==2:
        return idx, min(values)

    elif T==3:
        return idx, max(values)

    elif T == 5:
        if values[0]>values[1]: return idx, 1
        else: return idx, 0

    elif T == 6:
        if values[0]<values[1]: return idx, 1
        else: return idx, 0

    elif T == 7:
        if values[0] == values[1]: return idx, 1
        else: return idx, 0


    #return idx, val
print(parse_packet(initializationen(), 0))
