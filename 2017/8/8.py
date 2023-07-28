file=open("input8.txt", "r")

def compare( znamienko, first, second ):
    if znamienko == '==':
        return first == second
    if znamienko == '>':
        return first > second
    if znamienko == '<':
        return first < second
    if znamienko == '>=':
        return first >= second
    if znamienko == '<=':
        return first <= second
    if znamienko == '!=':
        return first != second


def funkcia():
    seckymena=[]
    polenul=[]
    all_lines=[]
    for r in file:
        r=r.strip()
        line=r.split(" ")
        all_lines.append(line)

        namefirst = line[0]
        if namefirst not in seckymena:
            seckymena.append(namefirst)

    for i in range(26+1): #co je len(seckymena)
       polenul.append(0)
    for namefirst in line:
        seckymena.append(namefirst)

    registre=dict(zip(seckymena, polenul))

    for line in all_lines:
        namefirst=line[0]
        namesecond=line[4]
        inc_dec=1 if line[1] ==  'inc' else -1
        first_value=int(line[2])
        second_value=int(line[-1])
        znamienko=line[-2]
        if compare( znamienko, registre[namesecond] ,second_value):
             registre[namefirst] += inc_dec* first_value



    print(seckymena)
    print(r)
    print(registre)

print (funkcia())