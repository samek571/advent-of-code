import copy

allpaths=[]

def parsing():
    everything={}
    moves=open("input12.txt").read().split("\n")
    moves.pop()

    for i in moves:
        i=i.split("-")
        if i[0] in everything: everything[i[0]]+=[i[1]]
        elif i[0] not in everything: everything[i[0]]=[i[1]]

        if i[1] in everything:
            everything[i[1]]+=[i[0]]
        else:
            everything[i[1]]=[i[0]]

    print(everything)

    return everything
    # new=copy.deepcopy(everything)
    # for key, val in everything.items():
    #     if key.islower() and len(val)==1:
    #         del new[key]
    #         for i in new[val[0]]:
    #             if i == key:
    #                 new[val[0]].remove(i)
    #
    #
    # return new

print(parsing())



#def f(graph, 'start', []):



def f(graph, node, path):

    path=path+[node]
    for n in graph[node]:
        if n=='end':
            allpaths.append(path+['end'])
        else:
            if n.isupper() or n not in path:
                f(graph,n,path)

print(f(parsing(),'start',[] ))

import pprint
pprint.pprint(allpaths)
print(len(allpaths))