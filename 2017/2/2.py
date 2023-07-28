file=open("input2.txt", "r")

def prostredie():
    checksum=0
    for r in file:
        r=r.strip()
        r=r.split()
        r = [int(i) for i in r]
        r.sort()

        difference= r[-1] - r[0]
        checksum+=difference

        # print(difference)
        # print(r)

    return(checksum)

print(prostredie())