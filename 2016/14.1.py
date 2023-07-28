import hashlib

def fx(strink):
    output=0
    i=0

    while True: #output<65:
        temporar = strink+str(i)

        randomn = hashlib.md5(temporar.encode())
        randomn = randomn.hexdigest()

        washere=False
        for y in range(2,len(randomn)):

            if randomn[y] == randomn[y-1] == randomn[y-2]:
                fivedigits = randomn[y]*5

                for counter in range(1, 1001):
                    temptemp = strink + str(i+counter)
                    another = hashlib.md5(temptemp.encode())
                    another = another.hexdigest()

                    if fivedigits in another:
                        output+=1
                        if output==64: return i
                        break

                washere=True

            if washere == True: break

        i+=1

print(fx("abc"))
print(fx("zpqevtbw"))
