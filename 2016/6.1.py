moves = open("input6.txt").read().split("\n")

def fx(moves):
    output=''
    i=0
    while i!=len(moves[0]):
        dick = {}
        for letter in range(len(moves)-1):
            letter = moves[letter][i]

            if letter in dick: dick[letter]+=1
            else: dick[letter]=1

        #sort_dict = dict(sorted(dick.items(), key=lambda x: x[1]), reverse=True)
        output+=max(dick, key= lambda x: dick[x])

        i+=1

    return output

print(fx(moves))