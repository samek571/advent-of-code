def parsing():
    moves_help = open("input9.txt").read().split("\n")
    moves_help.pop()

    moves = []
    for i in moves_help:
        helpi = []
        for char in i: helpi.append(int(char))
        moves.append(helpi)

    return moves


print(parsing())


def fx(moves):
    risk_sum = 0

    counter_line = 0
    for line in moves:
        counter_digit = 0
        for digit in line:

            # horny riadok bez rohov
            if (counter_line == 0) and (0 < counter_digit < len(line) - 1):
                if digit < moves[counter_line][counter_digit - 1] and \
                        digit < moves[counter_line][counter_digit + 1] and \
                        digit < moves[counter_line + 1][counter_digit]: risk_sum += digit + 1

                # dolny riadok bez rohov
            elif counter_line == len(moves) - 1 and (0 < counter_digit < len(line) - 1):
                if digit < moves[counter_line][counter_digit - 1] and \
                        digit < moves[counter_line][counter_digit + 1] and \
                        digit < moves[counter_line - 1][counter_digit]: risk_sum += digit + 1


            # secko bez rohov
            elif 0 < counter_line < len(moves) - 1:
                # lavy stlpec
                if counter_digit == 0:
                    if digit < moves[counter_line + 1][counter_digit] and \
                            digit < moves[counter_line][counter_digit + 1] and \
                            digit < moves[counter_line - 1][counter_digit]: risk_sum += digit + 1


                # pravy stlpec
                elif counter_digit == len(line) - 1:
                    if digit < moves[counter_line + 1][counter_digit] and \
                            digit < moves[counter_line][counter_digit - 1] and \
                            digit < moves[counter_line - 1][counter_digit]: risk_sum += digit + 1

                # stred bez picovin
                else:
                    if digit < moves[counter_line + 1][counter_digit] and \
                            digit < moves[counter_line][counter_digit - 1] and \
                            digit < moves[counter_line][counter_digit + 1] and \
                            digit < moves[counter_line - 1][counter_digit]: risk_sum += digit + 1

            # rohy
            # else:
            #     if counter_line==0 and counter_digit==0:
            #         if digit < moves[counter_line - 1][counter_digit] and \
            #             digit < moves[counter_line][counter_digit + 1]: risk_sum += digit+1
            #
            #     elif counter_line==0 and counter_digit==len(line)-1:
            #         if digit < moves[counter_line - 1][counter_digit] and \
            #             digit < moves[counter_line][counter_digit - 1]: risk_sum += digit+1
            #
            #     elif counter_line==len(moves)-1 and counter_digit==0:
            #         if digit < moves[counter_line + 1][counter_digit] and \
            #             digit < moves[counter_line][counter_digit + 1]: risk_sum += digit+1
            #
            #     elif counter_line==len(moves)-1 and counter_digit==len(line)-1:
            #         if digit < moves[counter_line + 1][counter_digit] and \
            #             digit < moves[counter_line][counter_digit - 1]: risk_sum += digit+1

            print(counter_digit)
            counter_digit += 1
        counter_line += 1

    return risk_sum


print(fx(parsing()))
