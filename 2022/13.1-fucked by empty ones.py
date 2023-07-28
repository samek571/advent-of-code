import re
import collections

def inputting(s):
    matrix=open(s).read().split("\n")
    matrix.pop()
    return matrix

def fx(s):
    matrix = inputting(s) ; res=[]

    for i in range(0, len(matrix), 3):
        #first = collections.deque(re.findall("\d+", matrix[i])) ; second = collections.deque(re.findall("\d+", matrix[i+1]))
        first = collections.deque(int(num) for num in re.findall("\d+", matrix[i+0]))
        second = collections.deque(int(num) for num in re.findall("\d+", matrix[i+1]))

        # case 7
        if not first and not second:
            if len(matrix[i]) < len(matrix[i+1]): res.append(i//3+1)
            else: res.append(0)

        #shortening
        while first and second and first[0] == second[0]:
            first.popleft() ; second.popleft()


        #case 4 6
        if not first and second: res.append(i//3+1)
        # case 5
        #elif first and not second: res.append(0)
        elif first and second:
            # case 1 2
            if first[0]<second[0]: res.append(i//3+1)
            # case 3 8
            #else: res.append(0)


    return sum(res), res




#print(fx(s='input13hh.txt'))
#print(fx(s='input13h.txt'))
print(fx(s='input13.txt')) #5600 too high ; 5448 too low


# s = '[[[8,[10]],7],[[4,[2,0,10,9,6]]]]'
# print(re.findall("\d+", s))