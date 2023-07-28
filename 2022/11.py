import re

def inputting(s):
    moves=open(s).read().split("\n")
    moves.pop()

    items = []
    # ((*, 19), 23, (2, 3))
    decision = []


    for idx in range(0, len(moves), 7):
        x= re.findall("\d+", moves[idx+1])
        for i in range(len(x)): x[i] = int(x[i])
        items.append(x)


        rd = moves[idx+2].split()
        if rd[-1] == "old": rd=("**", 2)
        else: rd=(rd[-2], int(rd[-1]))

        divisible = int(moves[idx+3].split()[-1])

        succ, fail = int(moves[idx+4].split()[-1]), int(moves[idx+5].split()[-1])


        decision.append((rd, divisible, (succ, fail)))



    return items, decision


def fx(s, cycles):
    items, decision = inputting(s)
    n, y = len(items), 0
    outputshit=[0 for _ in range(n)]
    print(decision)
    print(items)


    while y<cycles:
        y+=1
        for i in range(n):
            outputshit[i]+=len(items[i])

            while items[i]:
                item = items[i].pop()
                result = (eval(str(item) + decision[i][0][0] + str(decision[i][0][1]))) //3

                if result%decision[i][1]==0:items[decision[i][2][0]].append(result)
                else: items[decision[i][2][1]].append(result)



        print(outputshit)




    outputshit.sort()
    return outputshit[-2] * outputshit[-1]


print(fx("input11h.txt", 20))
print(fx("input11h.txt", 10000))
print(fx("input11.txt", 20))
print(fx("input11.txt", 10000))



"""
def fx(s):
    items, decision = inputting(s)
    n, y = len(items), 0
    outputshit=[0 for _ in range(n)]
    print(decision)
    print(items)


    while y<21:
        y+=1
        tmp = [[] for _ in range(n)]
        for i in range(n):
            outputshit[i]+=len(items[i])

            while items[i]:
                item = items[i].pop()
                result = (eval(str(item) + decision[i][0][0] + str(decision[i][0][1]))) //3

                if result%decision[i][1]==0:tmp[decision[i][2][0]].append(result)
                else: tmp[decision[i][2][1]].append(result)



        print(outputshit)
        items = tmp




    outputshit.sort()
    return outputshit[-2] * outputshit[-1]

"""