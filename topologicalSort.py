class TopologicalSort:
    def __init__(self, adjLists):
        self.adjLists = adjLists
        self.sortedV = []

    def sort(self):
        for v in self.adjLists.keys():
            if v not in self.sortedV:
                self.helper(v)
        return self.sortedV[::-1]
            

    def helper(self, start):
        if start in self.adjLists:
            for v in self.adjLists[start]:
                if v not in self.sortedV:
                    self.helper(v)
        self.sortedV.append(start)
            
                
    


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"]
}


test = TopologicalSort(graph)
print test.sort()

