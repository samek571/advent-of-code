inp = open("input20.txt").read().split("\n")
inp.pop()


from functools import reduce

def fx(inp):
    own_inp = []

    #partitioning onto inp
    for line in inp:
        a, b = [int(i) for i in line.strip().split("-")]
        own_inp.append([a, b])
    own_inp.sort()


    output = []
    output.append(own_inp.pop(0))
    while (own_inp):
        if output[-1][-1] >= own_inp[0][0]-1:
            output[-1][-1] = max(output[-1][-1], own_inp[0][1])
            own_inp.pop(0)
        else:
            output.append(own_inp.pop(0))

    print(len(output)-1) #-1 because he len is of the actual intervals and the numbers inbetween them
    # are one short since its [] ip [] ip [] ... the len is 3 but just 2 ips are not prohibited
    return output

print(fx(inp))