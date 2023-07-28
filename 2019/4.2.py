def maslo():
    qualified=0
    for i in range (266666, 800000): #(264793, 803935+1):
        i=str(i)
        for m in range(0, len(i) - 1):  #monotonnost
            if i[m] > i[m + 1]:
                break
        else:
            counter = 0
            for n in range(len(i)-1):   #2rovnake po sebe ktore nie su subset viac rovnakych posebe
                if i[n] == i[n+1]:
                    counter+=1
                elif counter==1:
                    qualified+=1
                    print(i)
                    break
                else:
                    counter=0
#missing 266677 266688 266699
    return(qualified)
print(maslo())
#510 513
