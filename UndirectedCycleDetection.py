class CycleDetection:
    def __init__(self, adjLists):
        self.adjLists = adjLists
        self.visited = []
        self.cycle = False

    def hasCycle(self):
        for v in self.adjLists.keys():
            if v not in self.visited:
                self.visited.append(v)
                self.helper(v, None) 
        return self.cycle

    def helper(self, start, parent):
        for v in self.adjLists[start]:
            if v not in self.visited:
                self.visited.append(v)
                self.helper(v, start)
            else:
                if v != parent:
                    self.cycle = True
    


graph = {
        "s": ["a", "x"],
        "a": ["s", "z"],
        "z": ["a"],
        "x": ["s", "d"],
        "d": ["x", "c", "f"],
        "c": ["d"],
        "f": ["d", "v"],
        "v": ["f"]
}

test = CycleDetection(graph)
print test.hasCycle()
