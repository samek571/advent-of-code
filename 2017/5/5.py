file=open("input5.txt", "r")

def funkcia():
    plocha=[]
    for r in file:
        r=int(r.strip())
        plocha.append(r)

    pozicia=0
    n=0
    while pozicia < len(plocha) and pozicia >= 0:
        old_pozicia = pozicia
        pozicia += plocha[pozicia]
        plocha[old_pozicia] += 1
        n += 1
    return n

print( funkcia() )