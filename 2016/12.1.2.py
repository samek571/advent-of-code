moves=open("input12.txt").read().split("\n")
moves.pop()

def fx(moves):
    regis = {"a":0, "b":0, "c":0, "d":0}
    #regis = {"a":0, "b":0, "c":1, "d":0}

    print(len(moves))
    i=0
    while i<len(moves):
        line = moves[i]

        if "inc" in line: regis[line[-1]]+=1
        elif "dec" in line: regis[line[-1]]-=1

        elif "cpy" in line:
            if line[4].isnumeric() == True:
                num=0
                if len(line)==7: num = int(line[4])
                elif len(line)==8: num = int(line[4:6])

                regis.update({line[-1] : num})
            else: regis.update({line[-1] : int(regis[line[-3]])})

        else: #jnz
            num=int(line[-1])
            if "-" in line: num = -1*int(line[-1])

            checking = line[4]
            if checking.isnumeric() == True: checking = int(checking)
            else: checking = regis[line[4]]

            if checking != 0:
                i+=num
                continue


        i+=1
    return regis

print(fx(moves))