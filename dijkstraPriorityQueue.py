import heapq

class Dijkstra:
    def __init__(self, graph, startingVertex):
        self.graph = graph
        self.distances = {vertex: float('inf') for vertex in graph}
        self.distances[startingVertex] = 0

    def calculateShortestDistance(self):
        pq = []
        entry_lookup = {}
        
        for vertex, distance in self.distances.items():
            entry = [distance, vertex]
            entry_lookup[vertex] = entry
            heapq.heappush(pq, entry)

        while(pq):
            currentDistance, currentVertex  = heapq.heappop(pq)
            print currentDistance, currentVertex
            
            for neighbor, neighborDistance in self.graph[currentVertex].items():
                distance = self.distances[currentVertex] + neighborDistance
                if distance < self.distances[neighbor]:
                    self.distances[neighbor] = distance
                    entry_lookup[neighbor][0] = distance
            heapq.heapify(pq)
        return self.distances
        

graph = {
    'A': {'B': 4, 'C': 3, 'E': 7},
    'B': {'A': 4, 'C': 6, 'D': 5},
    'C': {'A': 3, 'B': 6, 'D': 11, 'E': 8},
    'D': {'B': 5, 'C': 11, 'E': 2, 'F': 2, 'G': 10},
    'E': {'A': 7, 'C': 8, 'D': 2, 'G': 5},
    'F': {'D': 2, 'G': 3},
    'G': {'D': 10, 'E': 5, 'F': 3}
}
startingVertex = 'A'
test = Dijkstra(graph, startingVertex)
print test.calculateShortestDistance()
