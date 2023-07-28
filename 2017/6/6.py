import time

def funkcia():
    start_time=time.time()
    allbanks=[]
    #banky=[0,2,7,0] #tesovacie
    banky=[10,3,15,10,5,15,5,15,9,2,5,8,5,2,3,6]
    allbanks=[banky.copy()]

    while True:
        biggest=-1
        for i in banky:
            if biggest < i:
                biggest=i   # tu by sme mali vediet hodnotu najvacsieho prvku v bankach


        for prvanajvacsia in range(0,len(banky)):
            if banky[prvanajvacsia]==biggest:
                banky[prvanajvacsia]=0
                break       # tu by sme mali vediet hodnotu a poziciu najvacsieho prvku v bankach, vzapati sa hodnota nuluje

        i=prvanajvacsia
        while biggest >0:
            # zaciatok na prvej najvacsej pozicii+1, odtadial zacneme behat po bankach a vzdy spravime value+1, dokopy biggestkrat
            i = (i+1)%len(banky)
            biggest -= 1
            banky[i] += 1

        if banky in allbanks:
            end_time=time.time()
            return len(allbanks), banky, end_time-start_time
        else:
            allbanks.append(banky.copy())

print(funkcia())