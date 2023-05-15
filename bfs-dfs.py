from collections import deque


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited = set()
        visited.add(vertex)
        queue = deque()
        queue.append(vertex)
        while queue:
            the_vertex = queue.popleft()
            print(the_vertex)
            for adjacent in self.gdict[the_vertex]:
                if adjacent not in visited:
                    visited.add(adjacent)
                    queue.append(adjacent)

    def dfs(self, vertex):
        visited = set()
        stack = [vertex]
        while stack:
            the_vertex = stack.pop()
            if the_vertex in visited:
                continue
            visited.add(the_vertex)
            for adjacent in self.gdict[the_vertex]:
                    stack.append(adjacent)

    def dfs_1(self, vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(vertex)
        for adjacent in self.gdict[vertex]:
            if adjacent not in visited:
                self.dfs_1(adjacent, visited)

    visited = rec_stack = set()

    def dfs_for_cycle_detection(self, start, visited, rec_stack):
        visited.add(start)
        rec_stack.add(start)
        for adjacent in self.gdict[start]:
            if adjacent not in visited:
                if self.dfs_for_cycle_detection(adjacent, visited, rec_stack):
                    return True
            elif adjacent in rec_stack:
                return True
        rec_stack.remove(start)
        return False







