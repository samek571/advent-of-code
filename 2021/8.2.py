def parsing():
    moves=open("input8.txt").read().split("\n")
    moves.pop()
    return moves

def fx(moves):
    output=0
    for line in moves:
        line = line.replace("|", " ")
        line = line.split()

        ciganskyaudit={0:'', 1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:'', 9:''}
        number=''
        sexta=[]
        quinta=[]

        for i in line[:-4]:
            if len(i)==7: ciganskyaudit[8]=''.join(sorted(i))
            elif len(i)==2: ciganskyaudit[1]=''.join(sorted(i))
            elif len(i)==4: ciganskyaudit[4]=''.join(sorted(i))
            elif len(i)==3: ciganskyaudit[7]=''.join(sorted(i))
            elif len(i) == 6: sexta.append(''.join(sorted(i)))
            elif len(i) == 5: quinta.append(''.join(sorted(i)))

        #finding 9
        for element_len6 in sexta:
            counter=0
            for char in ciganskyaudit[4]:
                if char in element_len6: counter+=1

            if counter == 4:
                ciganskyaudit[9] = element_len6
                sexta.remove(element_len6)
                break

        #finfing pixel
        nine=ciganskyaudit[9]
        eight=ciganskyaudit[8]
        eight = ''.join(sorted(eight))
        nine = ''.join(sorted(nine))
        i=0
        while i<len(nine) and eight[i] == nine[i]: i+=1
        pixel = eight[i]

        # finding 0
        for element_len6 in sexta:
            counter=0
            for char in ciganskyaudit[1]:
                if char in element_len6: counter+=1

            if counter == len(ciganskyaudit[1]):
                ciganskyaudit[0] = element_len6
                sexta.remove(element_len6)

        #finding 6
        ciganskyaudit[6] = sexta[0]

        #finding 3
        for element_len5 in quinta:
            counter=0
            for char in ciganskyaudit[1]:
                if char in element_len5: counter+=1

            if counter == len(ciganskyaudit[1]):
                ciganskyaudit[3] = element_len5
                quinta.remove(element_len5)

        #finding 2 and 5
        if pixel in quinta[0]:
            ciganskyaudit[2] = quinta[0]
            ciganskyaudit[5] = quinta[-1]
        else:
            ciganskyaudit[2] = quinta[-1]
            ciganskyaudit[5] = quinta[0]



        #final number for specific line
        for i in line[10:]:
            i="".join(sorted(i))
            for key, val in ciganskyaudit.items():
                if i == val: number+=str(key)

        print(number)
        output+=int(number)

    return output

print(fx(parsing()))
