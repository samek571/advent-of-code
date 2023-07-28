moves = open("input7.txt").read().split("\n")

def fx(moves):

    output=0
    for line in moves:
        l=len(line)
        i=0

        quote=False
        innit=False

        while i <= l-4:
            substring=line[i:i+4]
            if "[" == substring[-1]:
                innit = True
                i+=4
                continue

            elif "]" == substring[-1]:
                innit = False
                i+=4
                continue

            if substring[0] == substring[-1] and substring[1] == substring[2] and substring[0] != substring[1]:
                if innit == False: quote=True
                else:
                    quote=False
                    break

            i+=1

        if quote==True: output+=1


    return output
print(fx(moves))
#122 too high