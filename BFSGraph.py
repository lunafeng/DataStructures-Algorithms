class BFS:
    def __init__(self, adjLists):
        self.adjLists = adjLists

    def tranverse(self, start):
        level = {start: 0}
        parent = {start: None}
        i = 1
        frontier = [start]
        while(frontier):
            next = []
            for u in frontier:
                for v in self.adjLists[u]:
                    if v not in level:
                        level[v] = i
                        parent[v] = u
                        next.append(v)
            frontier = next
            i += 1
        levels = list(set(level.values()))
        levels.sort()
        for l in levels:
            print "level: ", l
            for k in level:
                if level[k] == l:
                    print "nodes: ", k,
            print "\n"

graph = {
        "s": ["a", "x"],
        "a": ["s", "z"],
        "z": ["a"],
        "x": ["s", "d", "c"],
        "d": ["x", "c", "f"],
        "c": ["x", "d", "f"],
        "f": ["d", "c", "v"],
        "v": ["c", "f"]
}

test = BFS(graph)
test.tranverse("s")
