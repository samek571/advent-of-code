moves=open("input8.txt").read().split("\n")
moves.pop()

def fx(moves, u, v):
    cig=["."]*u
    for i in range(len(cig)):
        cig[i] = ["."]*v

    konter=0

    while konter != len(moves):
        line = moves[konter]

        if "rect" in line:
            position=''

            i=5
            while line[i].isnumeric():
                position+=line[i]
                i+=1
            i+=1

            position = int(position)
            movement = int(line[i:])

            for y in range(movement):
                for x in range(position):
                    cig[y][x] = "#"

        else:
            position = ''
            second_temp = ''
            idx=line.find("=")

            i=idx+1
            while line[i].isnumeric():
                position += line[i]
                i += 1

            i=len(line)-1
            while line[i].isnumeric():
                second_temp += line[i]
                i -= 1

            position = int(position)
            movement = int(second_temp[::-1])


            if "row" in line:
                row = cig[position]
                for hovno in range(movement):
                    row = [row.pop()] + row

                cig[position] = row


            else:

                all_el_in_column=[]

                for column in range(len(cig)):
                    all_el_in_column.append(cig[column][position])

                for hovno in range(movement):
                    all_el_in_column = [all_el_in_column.pop()]+all_el_in_column

                for column in range(len(cig)):
                    cig[column][position] = all_el_in_column[column]


        for i in cig:
            print(i)
        print(konter+1, line)

        konter += 1


    output = 0
    for row in range(len(cig)):
        for col in range(len(cig[0])):
            if cig[row][col] == "#":
                output+=1

    return output

print(fx(moves, 6, 50))
#print(fx(moves, 7, 7))

#102 and 110 too low