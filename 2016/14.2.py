import hashlib
import sys


hashes=dict()

def hash2016(s,index):

    tmp=s+str(index)
    for _ in range(2017):
        tmp = hashlib.md5(tmp.encode('utf-8')).hexdigest()
    return tmp


def fx(s):
    n_keys=0
    for index in range(0,99999999):

        if index not in hashes:
            h=hash2016(s,index)
            hashes[index]=h
        else:
            h=hashes[index]

        for j in range(2, len(h)):

            if h[j] == h[j-1] == h[j-2]:
                fivedigits = h[j]*5
                #print(i,first_2016[y], y, first_2016, fivedigits)


                for k in range(1, 1001):
                    if (index+k) not in hashes.keys():
                        hashes[index+k]=hash2016(s,index+k)

                    if fivedigits in hashes[index+k]:
                        n_keys+=1
                        print("XXXXX",n_keys, index, h, )
                        if n_keys==64: return index
                        break

                break


#print(fx("abc"))
print(fx("zpqevtbw"))
#too low 21631 and 13663