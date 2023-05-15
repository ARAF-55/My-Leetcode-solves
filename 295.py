import heapq


class MedianFinder:

    def __init__(self):
        self.max_heap = [float("inf")]
        self.min_heap = [float("inf")]

    def addNum(self, num: int) -> None:
        if num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        if abs(len(self.max_heap) - len(self.min_heap)) > 1:
            if len(self.max_heap) > len(self.min_heap):
                value = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, -value)
            else:
                value = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -value)

    def findMedian(self) -> float:
        total = len(self.min_heap) + len(self.max_heap)
        if total % 2 == 1:
            if len(self.min_heap) > len(self.max_heap):
                return float(self.min_heap[0])
            else:
                return float(-self.max_heap[0])
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2


obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
print(obj.findMedian())