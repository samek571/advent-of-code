def maslo():
    qualified=0
    for i in range (264793, 803935+1):
        i=str(i)
        print(i)
        if "33" in i or "44" in i or "55" in i or "66" in i or "77" in i or "88" in i or "99" in i:
            for n in range(len(i) - 1):
                if i[n] > i[n+1]:
                    break
            else:
                qualified += 1
                continue

    return(qualified)
print(maslo())