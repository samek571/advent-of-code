import copy
def parsing():
    moves_help=open("input9.txt").read().split("\n")
    moves_help.pop()
    
    moves=[]
    for i in moves_help:
        helpi=[]
        for char in i: helpi.append(int(char))
        moves.append(helpi)
    return moves


def fx(moves):
    neww=copy.deepcopy(moves)


    counter_line=0
    for line in moves:
        counter_digit=0
        for digit in line:

            if digit == 9:
                neww[counter_line][counter_digit]="|"


            # horny riadok bez rohov
            if (counter_line==0) and (0<counter_digit<len(line)-1):
                if digit < moves[counter_line][counter_digit-1] and\
                    digit < moves[counter_line][counter_digit+1] and \
                    digit < moves[counter_line+1][counter_digit]: neww[counter_line][counter_digit]="_"


                #dolny riadok bez rohov
            elif counter_line==len(moves)-1 and (0<counter_digit<len(line)-1):
                if digit < moves[counter_line][counter_digit-1] and\
                    digit < moves[counter_line][counter_digit+1] and \
                    digit < moves[counter_line-1][counter_digit]: neww[counter_line][counter_digit]="_"


            #secko bez rohov
            elif 0<counter_line<len(moves)-1:
                #lavy stlpec
                if counter_digit==0:
                    if digit < moves[counter_line + 1][counter_digit] and \
                        digit < moves[counter_line][counter_digit + 1] and \
                        digit < moves[counter_line - 1][counter_digit]: neww[counter_line][counter_digit]="_"


                #pravy stlpec
                elif counter_digit == len(line)-1:
                    if digit < moves[counter_line + 1][counter_digit] and \
                        digit < moves[counter_line][counter_digit - 1] and \
                        digit < moves[counter_line - 1][counter_digit]: neww[counter_line][counter_digit]="_"

                #stred bez picovin
                else:
                    if digit < moves[counter_line + 1][counter_digit] and \
                        digit < moves[counter_line][counter_digit - 1] and \
                        digit < moves[counter_line][counter_digit + 1] and \
                        digit < moves[counter_line - 1][counter_digit]: neww[counter_line][counter_digit]="_"


            counter_digit+=1
        counter_line+=1

    return neww

def printaz(neww):
    for line in neww:
        for char in range (len(line)):

            line[char]= str(line[char])

    for line in neww:
        line = ''.join(line)
        print(line)


print(printaz(fx(parsing())))