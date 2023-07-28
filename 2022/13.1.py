import re
import collections

def inputting(s):
    matrix=open(s).read().split("\n")
    matrix.pop()
    return matrix

def compare(left, right):
    if not isinstance(left, list):
        left = [left]
    if not isinstance(right, list):
        right = [right]
    for l, r in zip(left, right):
        if isinstance(l, list) or isinstance(r, list):
            res = compare(l, r)
        else:
            res = r - l
        if res != 0:
            return res
    return len(right) - len(left)

def fx(s):
    matrix = inputting(s) ; res=[]

    for i in range(0, len(matrix), 3):
        a,b = eval(matrix[i]), eval(matrix[i+1])

        if compare(a,b) > 0:
            res.append(i//3+1)


    print(res)
    return sum(res)


#print(fx(s='input13hh.txt'))
#print(fx(s='input13h.txt'))
print(fx(s='input13.txt')) #5600 too high ; 5448 too low


# s = '[[[8,[10]],7],[[4,[2,0,10,9,6]]]]'
# print(re.findall("\d+", s))