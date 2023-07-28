file=open("input4.txt", "r")

def check_dupl_single(w1,w2):
    if len(w1) != len(w2):
        return False
    if ''.join(sorted(w1)) == ''.join(sorted(w2)):
        return True

    return False



def check_dupl( w1, x):
    for w2 in x:
        if check_dupl_single(w1,w2):
            return True
    return False

def gagor():
    submitnumber=0
    for line in file:
        chyba = 0
        line = line.strip()
        line = line.split()

        x=dict()
        dupl=False
        for w1 in line:
            if check_dupl( w1, x):
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