file=open("input5.txt", "r")

def funkcia():
    plocha=[]
    for r in file:
        r=int(r.strip())
        plocha.append(r)

    #plocha = [0, 3, 0, 1, -3]
    pozicia=0
    n=0
    while pozicia < len(plocha) and pozicia >= 0:
        old_pozicia = pozicia
        pozicia += plocha[pozicia]

        if pozicia-old_pozicia >= 3:
            plocha[old_pozicia] -= 1
        else:
            plocha[old_pozicia] += 1
        n += 1
    return n

print( funkcia() )