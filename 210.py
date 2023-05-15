from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visited = set()
        res = []
        for i in prerequisites:
            graph[i[1]].append(i[0])

        def topologicalSort(start, rec_stk):
            visited.add(start)
            rec_stk.add(start)
            for j in graph[start]:
                if j not in visited:
                    if topologicalSort(j, rec_stk):
                        return True
                elif j in rec_stk:
                    return True
            rec_stk.remove(start)
            res.append(start)
            return False

        for k in list(graph):
            if k not in visited:
                rec_stack = set()
                if topologicalSort(k, rec_stack):
                    return []
        if len(res) < numCourses:
            for v in range(numCourses):
                if v not in visited:
                    res.append(v)
        return res[::-1]
