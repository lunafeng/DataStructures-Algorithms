class DFS:
    def __init__(self, adjLists):
        self.adjLists = adjLists
        self.parents = {}

    def tranverseAll(self):
        for v in self.adjLists.keys():
            if v not in self.parents:
                print v
                self.parents[v] = None
                self.tranverseFrom(v)
                
    def tranverseFrom(self, start):
        for v in self.adjLists[start]:
            if v not in self.parents:
                print v 
                self.parents[v] = start
                self.tranverseFrom(v)

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

test = DFS(graph)
test.tranverseAll()
