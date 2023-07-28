moves = open("input7.txt").read().split("\n")

def fx(moves):

    output=0

    for line in moves:
        secko=set()
        l=len(line)
        i=0

        quote=False
        innit=False

        while i <= l-3:
            substring=line[i:i+3]
            if "[" == substring[-1]:
                innit = True
                i+=3
                continue

            elif "]" == substring[-1]:
                innit = False
                i+=3
                continue

            if substring[0] == substring[-1]  and substring[0] != substring[1] and innit == True:

                appendovac=''
                appendovac+=substring[1]
                appendovac+=substring[0]
                appendovac+=substring[1]

                secko.add(appendovac)

            i+=1

        i=0
        while i <= l-3:
            substring=line[i:i+3]
            if "[" == substring[-1]:
                innit = True
                i+=3
                continue

            elif "]" == substring[-1]:
                innit = False
                i+=3
                continue

            if substring[0] == substring[-1] and substring[0] != substring[1] and innit == False:
                if substring in secko:
                    output+=1
                    break

            i+=1


    return output
print(fx(moves))
#1516 too high