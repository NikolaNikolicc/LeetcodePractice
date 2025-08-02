# https://www.youtube.com/watch?v=itmhHWaHupI

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        if self.minHeap and self.minHeap[0] < -self.maxHeap[0]:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        if len(self.minHeap) - len(self.maxHeap) > 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
        if len(self.maxHeap) - len(self.minHeap) > 1:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

    def findMedian(self) -> float:
        if not self.minHeap and not self.maxHeap:
            return -1

        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]

        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]

        return float(self.minHeap[0] - self.maxHeap[0]) / 2
        
        