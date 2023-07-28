moves=open("input3.txt").read().split("\n")
moves.pop()

def fx(moves):
    print(len(moves))

    gama=''
    i=j=0
    while i< len(moves[0]):
        number_of_1 = 0
        while j< len(moves)-1:
            if moves[j][i] == "1": number_of_1+=1
            print(i, j, number_of_1)
            j+=1

        if number_of_1>=len(moves)//2: gama+="1"
        else: gama+="0"

        j=0
        i+=1

    epsi=''
    for i in gama:
        if i == "1": epsi+='0'
        else: epsi+="1"

    gama=(int(gama, 2))
    epsi=(int(epsi, 2))

    return gama * epsi

print(fx(moves))