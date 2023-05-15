from collections import defaultdict


class Graph:
    def __init__(self, numberOfVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalSortUtil(self, v, visited):
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited)
        visited.insert(0, v)

    def topoLogicalSort(self):
        visited = []
        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k, visited)
        return visited


customGraph = Graph(8)
customGraph.addEdge("A", "C")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "H")
customGraph.addEdge("E", "F")
customGraph.addEdge("F", "G")
customGraph.addEdge("B", "D")
customGraph.addEdge("B", "C")
customGraph.addEdge("D", "F")

print(customGraph.topoLogicalSort())
