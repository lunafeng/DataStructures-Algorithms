class CycleDetection:
    def __init__(self, adjLists):
        self.adjLists = adjLists
        self.visited = []
        self.curVisit = []
        self.cycle = False

    def hasCycle(self):
        for v in self.adjLists.keys():
            if v not in self.visited:
                self.visited.append(v)
                self.curVisit = [v]
                self.helper(v) 
        return self.cycle

    def helper(self, start):
        if start in self.adjLists:
            for v in self.adjLists[start]:
                if v not in self.curVisit:
                    self.curVisit.append(v)
                else:
                    self.cycle = True
                if v not in self.visited:
                    self.visited.append(v)
                    self.helper(v)
                
    


graph = {
        "s": ["x"],
        "a": ["s", "z"],
        "x": ["d"],
        "d": ["c", "f"],
        "f": ["v"], 
        "v": ["d"]
}

test = CycleDetection(graph)
print test.hasCycle()
