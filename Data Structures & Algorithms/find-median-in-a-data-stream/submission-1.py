import heapq # to revise this as well

class MedianFinder: # to revise later

    def __init__(self):
        self.max_h, self.min_h = [], [] # small, large

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_h, -num)

        if self.max_h and self.min_h and (-self.max_h[0] > self.min_h[0]): # ensure max(small) <= min(large)
            heapq.heappush(self.min_h, -heapq.heappop(self.max_h))

        if len(self.max_h) > len(self.min_h) + 1:
            heapq.heappush(self.min_h, -heapq.heappop(self.max_h))
        elif len(self.min_h) > len(self.max_h):
            heapq.heappush(self.max_h, -heapq.heappop(self.min_h))

    def findMedian(self) -> float:
        if len(self.max_h) > len(self.min_h):
            return -self.max_h[0]
        return (-self.max_h[0] + self.min_h[0]) / 2
        