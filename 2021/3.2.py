moves=open("input3.txt").read().split("\n")
moves.pop()

def fx(moves):
    lenght = (len(moves[0]))

    i=j=0
    while i< lenght:
        number_of_1 = 0
        while j<= len(moves)-1:
            if moves[j][i] == "1": number_of_1+=1
            j+=1


        o2_eliminating=''
        if number_of_1>=len(moves)/2: o2_eliminating+='0' # for CO2 change to "1"
        else: o2_eliminating+='1'  # for CO2 change to "0"

        new=[]
        j=0
        while j<= len(moves)-1:
            print(i, j, "position",moves[j][i])
            if moves[j][i] != o2_eliminating:
                new.append(moves[j])
            j+=1
        print(new)


        if len(new)==2:
            #< if
            if int(new[-1],2) < int(new[0],2): return int(new[0],2)  # for CO2 change to ">"
            else: return int(new[-1],2)
        elif len(new)==1: return int(new[-1],2)
        else: moves=new

        j=0
        i+=1

    print(moves)
    return int(moves[-1],2)



print(fx(moves))

#2104 * 1979 = 4163816 too low
#2288 * 1920 = 4392960 too high
#2292 * 1920
#2024 * 2274
#2024 * 2090 = 4230160 :/
#2092 * 2031 = 4248852 :/
#2031 * 2104 = 4273224 :)