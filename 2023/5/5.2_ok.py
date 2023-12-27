import re

def preprocess(s):
    inp = open(s).read().split("\n")[:-1]
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

    return seeds, translations



seeds, almanac_zora = preprocess('input5h.txt')
minima = []
for i in range(1, len(seeds), 2):
    interval = [[seeds[i-1], seeds[i-1] + seeds[i]]]
    res = []
    for case in almanac_zora:
        while interval:
            start_range, end_range = interval.pop()
            for target, start, r in case:
                end = start + r
                offset = target - start
                
                # no overlap has no future
                if end <= start_range or end_range <= start: continue
                
                #make new interval
                if start_range < start:
                    interval.append([start_range, start])
                    start_range = start
                #make new interval aswell
                if end < end_range:
                    interval.append([end, end_range])
                    end_range = end

                res.append([start_range + offset, end_range + offset])
                break

            #if it hasnt been in forcycle
            else:
                res.append([start_range, end_range])
        
        #always keeping the latest set of intervals
        interval = res
        res = []


    minima += interval
print(min(loc[0] for loc in minima))