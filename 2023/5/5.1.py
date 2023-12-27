import re

inp = open('input5.txt').read().split("\n")[:-1]
seeds = list(map(int, re.findall('[0-9]+', inp[0])))

translations = []
converter = []
for line in inp[2:]:
    if not line:
        a = sorted(converter, key=lambda x: x[1])
        translations.append(a)
        converter = []
    elif "-" in line:
        continue
    else:
        converter.append(list(map(int, re.findall('[0-9]+', line))))

translations.append(converter)
#print(translations)

def alamnac_zora(seed):
    curr = seed

    for possibility in translations:
        for exchange in possibility:
            end, start, r = exchange
            if start<=curr<start+r:
                delta = end-start
                curr+=delta
                break

    return curr

def fx():
    return min([alamnac_zora(seed) for seed in seeds])
    #return [alamnac_zora(seed) for seed in seeds]
print(fx())