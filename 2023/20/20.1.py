import collections

def pre_p(s):
    graph = {}
    for line in open(s).read().strip().split('\n'):
        parts = line.split(" -> ")

        name = parts[0]
        ff = name.startswith("%")
        cnj = name.startswith("&")

        power = None
        if ff:
            power = False
            name = name[1:]
        elif cnj:
            power = {}
            name = name[1:]

        graph[name] = {
            "targets": parts[1].split(", "),
            "ff": ff,
            "cnj": cnj,
            "power": power
        }

    return graph


def fx(s):
    graph = pre_p(s)

    print(graph)
    for k, v in graph.items():
        if v["cnj"]:
            for a, b in graph.items():
                if k in b["targets"]:
                    v["power"][a] = False
    print(graph)

    low, high = 0, 0
    for _ in range(1000):
        q = collections.deque([("broadcaster", 0, None)])
        while q:
            curr, signal, inp = q.popleft()
            high, low = (high + 1, low) if signal else (high, low + 1)

            if curr not in graph: continue

            node, new_signal = graph[curr], signal
            if node["ff"]: #%
                if not signal:
                    graph[curr]["power"], new_signal = (False, 0) if node["power"] else (True, 1)
                else: continue #wont append shit

            elif node["cnj"]: #&
                node["power"][inp] = signal
                new_signal = 0 if all(node["power"].values()) else 1

            for target in node["targets"]:
                q.append((target, new_signal, curr))

    return low * high

print(fx('input20h.txt'))
