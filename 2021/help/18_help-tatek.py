def parsing(filename):
    rows=open(filename).read().split("\n")
    if len(rows[-1])==0:
        del rows[-1]
    return rows


def s_to_sfn(s):
    sfn = []
    incomplete = ''
    for ch in s:
        if ch in ('[',']',','):
            if incomplete != '':
                sfn.append(int(incomplete))
                incomplete = ''
            sfn.append(ch)
        else:
            incomplete = incomplete+ch
    return sfn


def sfn_to_s(sfn):
    s = ''
    for t in sfn:
        if t in ('[',']',','):
            s += t
        else:
            s += str(t)
    return s

def magnitude(s):
    while True:
        for i in range(len(s)):
            if s[i] == "," and s[i+1].isnumeric():
                left, right = i-1, i+1


                while s[left].isnumeric(): left-=1
                while s[right].isnumeric(): right+=1
                left+=1

                lnumber = s[left:i]
                rnumber = s[i+1: right]
                newnumber = str(3*int(lnumber) + 2*int(rnumber))
                s = s[:left-1] + newnumber + s[right+1:]

                if "[" and "]" not in s: return s
                else: break

def addition(s1, s2):
    return "[" + s1 + "," + s2 + "]"


def find_regular_number(sfn, start, direction):
    if direction == -1:
        for i in reversed(range(start)):
            rn = sfn[i]
            if rn not in ['[', ']', ',']:
                return i, rn
    else:
        for i in range(start+1,len(sfn)):
            rn = sfn[i]
            if rn not in ['[', ']', ',']:
                return i, rn
    return -1, 0

def explode(sfn):
    
    doexplode=False
    depth = 0
    for i, t in enumerate(sfn):
        if t == '[': depth += 1
        elif t == ']': depth -= 1
        elif t == ',': pass
        elif depth < 5: pass
        elif sfn[i+1] != ',': pass
        elif sfn[i+2] in ('[',']',','):
            pass
        else:
            doexplode=True
            break

    if not doexplode:
         return False

    #tu mame v 'i' index

    l, r = t, sfn[i+2]
    
    lrn_i, lrn = find_regular_number(sfn,i,-1)
    if lrn_i > 0:
        sfn[lrn_i] = lrn + l

    rrn_i, rrn = find_regular_number(sfn,i+2,1)
    if rrn_i > 0:
        sfn[rrn_i] = rrn + r
        
    sfn[i-1:i+4] = [0]
    return True

#print(explode( s_to_sfn("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")))
#print(explode("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"))
#print(explode("[[3,[2,[6,[7,3]]]],[8,[5,[4,[3,2]]]]]"))

def split_one(s):
    for i in range(len(s)):
        if s[i].isnumeric() and s[i+1].isnumeric():

            number = s[i] + s[i+1]
            firsthalf = str(int(number)//2)
            secondhalf = str(int(number)-int(firsthalf))
            number = addition(firsthalf, secondhalf)

            return True, s[:i] + number + s[i+2:]

    return False, s

def reduce_s(s):
    reduced = True
    while reduced  : 
        sfn=s_to_sfn(s)
        reduced = explode(sfn)
        if reduced:
            s=sfn_to_s(sfn)
            #print("exploded: ",s)
            continue
        reduced,s = split_one(s)
        if reduced:
            #print("splited: ",s)
            pass
    return s

#rows = parsing("test1.txt")
rows = parsing("input18.txt")

result=reduce_s(rows[0])
for row in rows[1:]:
    result=addition(result,row)
    result=reduce_s(result)

print(result)
print(magnitude(result))


max_mag = 0
for i1,row1 in enumerate(rows):
    for i2,row2 in enumerate(rows):
        if i1==i2: continue
        suma = reduce_s(addition(row1, row2))
        mag = int(magnitude(suma))
        if mag>max_mag:
            print(mag,max_mag,i1,i2,row1,row2)
        max_mag = max(max_mag, mag)

print( max_mag)
