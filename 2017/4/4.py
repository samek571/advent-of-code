file=open("input4.txt", "r")

def gagor():
    submitnumber=0
    for line in file:
        chyba = 0
        line = line.strip()
        line = line.split()

        x=dict()
        dupl=False
        for w1 in line:
            if w1 in x:
                dupl=True
                break
            x[w1]=1

        if dupl == False:
            submitnumber+=1
        # for w1 in line:
        #     for w2 in line:
        #         if w1 == w2:
        #             chyba+=1
        # if chyba <= len(line):
        #     submitnumber+=1

    return submitnumber
print(gagor())