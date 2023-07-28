import collections
import itertools

def inputting():
    ppl=open("input13pt2.txt").read().split("\n")
    if not ppl[-1]: ppl.pop()


    dick = dict()
    for shit in ppl:
        person = shit.split()[0]
        if person not in dick: dick[person] = collections.defaultdict(int)

    # for key in dick.keys():
    #     print('You would lose 0 happiness units by sitting next to ' + str(key) + ".")

    for general_truth in ppl:
        general_truth = general_truth.split()
        a,b, val = general_truth[0], general_truth[-1][:-1], int(general_truth[3])

        if general_truth[2] == "lose": val *=-1

        dick[a][b] += val
        dick[b][a] += val


    return dick


def fx():
    connections = inputting()

    tmp = []
    for key in connections.keys():
        tmp.append(key)

    ath=0
    for perm in list(itertools.permutations(tmp)):
        curr = 0
        for person_idx in range(len(tmp)):

            first, second = perm[person_idx], perm[person_idx-1]
            curr+=connections[first][second]

        ath = max(ath, curr)

    return ath

print(fx())