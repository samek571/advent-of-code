import re

def filterino(s):
    return [match for match in re.findall(r"\d+|-\d+|\{|\}|red|\[|\]", s)]


def sumazny_helper(s):
    return sum([int(match) for match in re.findall(r"\d+|-\d+", s)])



def dx(s):
    s = filterino(s)
    print(s)
    parentheezie=[]
    stack = []

    idx=0
    while idx!=len(s):
        item = s[idx]
        idx+=1

        if item in {"{", "["}:
            parentheezie.append(item)
            stack.append(item)

        elif item in {"}", "]"}:
            parentheezie.pop()

        elif item == "red" and parentheezie[-1]=="{":
            parentheezie.pop()
            
            while stack[-1] != "{": stack.pop()
            
            situation = 1
            tmpidx=idx
            while situation!=0:
                if s[tmpidx] == "{": situation+=1
                elif s[tmpidx] == "}": situation-=1
                tmpidx+=1

            idx = tmpidx
            

        else: stack.append(item)


    kokotput = ""
    for i in stack:
        kokotput+=i
        kokotput+=","

    print(stack)
    print(kokotput)
    return sumazny_helper(kokotput)

print(dx('[1,2,3]'))
print(dx('[1,{"c":"red","b":2},3]'))
print(dx('{"d":"red","e":[1,2,3,4],"f":5}'))
print(dx('[1,"red",5]'))


# stack till **red** occurs, then look if last prnths is { and if so,
# 1. pop stack till the { shows up
# 2. iterate junk till we dont scroll the whole subset of inficated {red}
# if last prnhts is [: we act as nothing happened

# if we get { or [ we add them in prnths stack

print(dx(s=open("input12.txt").read()))
#102148 too high
#96852 correct


# print(filterino("asd 45 5 -7"))
# print(filterino("asd 45 5 -7 {}"))
# print(filterino("asd 45 5 -7 {g}"))
# print(filterino("asd 45 5 -7 {g} red"))
# print(filterino("asd 45 5 -7 {g} re"))
# print("############################################################")

#print(filterino(open("input12.txt").read()))









'''
#part one
import re
def filterino(s):
    return sum([int(match) for match in re.findall(r"\d+|-\d+", s)])

print(filterino("asd 45 5 -7"))
print(filterino(open("input12.txt").read()))

'''