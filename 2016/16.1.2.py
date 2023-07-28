def fx(inp, disk):

    while len(inp)<disk:
        rev=inp
        inp+="0"

        for i in range(len(inp)-2, -1, -1):
            if rev[i] == "1": inp+="0"
            else: inp+="1"

    inp = inp[:disk]
    print(len(inp))

    ceskasuma(inp)

    #return checksum

def ceskasuma(inp):
    i=0
    checksum=''
    validator= {"00", "11"}
    while len(inp)%2==0 and i!=len(inp):
        digits = inp[i] + inp[i+1]

        if digits in validator: checksum+="1"
        else: checksum+="0"

        i+=2

    i=0
    inp=checksum
    if len(inp)%2==0:
        ceskasuma(checksum)
    else: print(checksum)


#print(fx("10000", 20))
#print(fx("10111100110001111", 272))
print(fx("10111100110001111", 35651584))