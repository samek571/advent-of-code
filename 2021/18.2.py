def parsing():
    moves=open("input18h.txt").read().split("\n")
    moves.pop()
    return moves

def s_to_sfn(s):
    slist=[]
    i=0
    while i < len(s):
        if s[i].isnumeric():
            number=s[i]
            u=i+1
            while s[u].isnumeric()==True:
                number+=s[u]
                u+=1

            slist.append(number)
            i=u
            continue


        else:
            slist.append(s[i])
            i+=1
    return slist

def sfn_to_s(listos):
    return ''.join(listos)


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
        for i in range(start + 1, len(sfn)):
            rn = sfn[i]
            if rn not in ['[', ']', ',']:
                return i, rn
    return -1, 0


def explode(sfn):
    doexplode = False
    depth = 0
    for i, t in enumerate(sfn):
        if t == '[':
            depth += 1
        elif t == ']':
            depth -= 1
        elif t == ',':
            pass
        elif depth < 5:
            pass
        elif sfn[i + 1] != ',':
            pass
        elif sfn[i + 2] in ('[', ']', ','):
            pass
        else:
            doexplode = True
            break

    if not doexplode:
        return False

    print(doexplode, i, t)
    # tu mame v 'i' index

    l, r = t, sfn[i + 2]

    lrn_i, lrn = find_regular_number(sfn, i, -1)
    if lrn_i > 0:
        sfn[lrn_i] = lrn + l

    rrn_i, rrn = find_regular_number(sfn, i + 2, 1)
    if rrn_i > 0:
        sfn[rrn_i] = rrn + r

    sfn[i - 1:i + 4] = [0]
    print(sfn)
    return True

#
# def explode(s):
#     s = s_to_sfn(s)
#     # print("")
#     # print(s)
#     depth = 0
#     for i in range (len(s)):
#         if s[i] == "[": depth+=1
#         elif s[i] == "]": depth-=1
#
#         if depth==5:
#
#             leftsnail = i+1
#             addingleft = i-1
#             while addingleft>0 and s[addingleft].isnumeric() == False: addingleft-=1
#             if addingleft!=0: leftnumber = str(int(s[addingleft])+int(s[leftsnail]))
#             else: leftnumber = ''.join(s[:i])
#
#             rightsnail = i+3
#             addingright = i+4
#             while addingright<len(s)-1 and s[addingright].isnumeric() == False: addingright+=1
#             if addingright!=len(s)-1: rightnumber = str(int(s[addingright])+int(s[rightsnail]))
#             else: rightnumber = "]"
#
#             #s[i:i+5] = [0]
#
#             if addingleft!=0 and addingright!=len(s)-1:
#                 return s[:addingleft] #+ leftnumber + ",0" + s[rightsnail+2: addingright] + rightnumber + s[addingright+1:]
#
#             elif addingleft==0 and addingright!=len(s)-1:
#                 return s[:addingleft] + leftnumber + "0," + rightnumber + s[addingright+1:]
#
#             elif addingleft!=0 and addingright == len(s)-1:
#                 return s[:addingleft] + leftnumber + ",0" + s[rightsnail+2: ]
#
#     return sfn_to_s(s)

#both ok
#print(explode("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"))
# print(explode("[[3,[2,[6,[7,3]]]],[8,[5,[4,[3,2]]]]]"))

#left missing
# print(explode("[[[[[9,8],1],2],3],4]"))
# print(explode("[[[[[9,8],3],2],3],4]"))

#right missing
#print(explode("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"))

#insufficient depth
#print(explode("[5,[7,[8,4]]]"))

def split_one(s):
    for i in range(len(s)):
        if s[i].isnumeric() and s[i+1].isnumeric():

            number = s[i] + s[i+1]
            firsthalf = str(int(number)//2)
            secondhalf = str(int(number)-int(firsthalf))
            number = addition(firsthalf, secondhalf)

            return s[:i] + number + s[i+2:]

    return s

def reduce_s(s):
    reduced = True
    while reduced:
        tmp = s
        s = explode(s)
        if s!=tmp:
            reduced = True
            print("exploded: ",s)
            continue
        else:
            reduced = False

        tmp=s
        s = split_one(s)
        if s != tmp:
            reduced = True
            print("splited: ",s)
        else:
            reduced = False
    return s

#print(reduce_s())

def fx():
    rows = parsing()

    result=reduce_s(rows[0])
    print(result)
    for row in rows[1:]:
        result=addition(result,row)
        result=reduce_s(result)
        print(result)

    return magnitude(result)

print(fx())





# print(magnitude("[[1,2],[[3,4],5]]"))
# print(magnitude("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"))
# print(magnitude("[[[[1,1],[2,2]],[3,3]],[4,4]]"))
# print(magnitude("[[[[3,0],[5,3]],[4,4]],[5,5]]"))
# print(magnitude("[[[[5,0],[7,4]],[5,5]],[6,6]]"))
# print(magnitude("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"))
# print(magnitude("[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]"))
