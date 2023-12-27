import networkx as nx

def pre_p(s):
    graph = nx.Graph()

    for line in open(s).read().strip().split("\n"):
        line = line.replace(": ", " ")
        line = line.split()
        for val in line[1:]:
            graph.add_edge(line[0], val, capacity=1.)

    return graph


def fx(s):
    graph = pre_p(s)

    cuts = nx.minimum_edge_cut(graph)
    graph.remove_edges_from(cuts)

    #believe or not, there is no fucking other way to multiply bunch of numbers in one liner without using lib
    return eval('*'.join(map(str, [len(partite) for partite in nx.connected_components(graph)])))


#witht the right tool, everything is possible
print(fx('input25.txt'))
# 555702