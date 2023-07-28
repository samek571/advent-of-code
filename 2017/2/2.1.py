file=open("input2.txt", "r")

def prostredie():
    sum=0
    for r in file:
        r=r.strip()
        r=r.split()
        r = [int(i) for i in r]
        r.sort()

        for a in r:
            for b in r:
                if a!=b:
                    if a%b==0:
                        sum+=a/b
        
    return(sum)

print(prostredie())
