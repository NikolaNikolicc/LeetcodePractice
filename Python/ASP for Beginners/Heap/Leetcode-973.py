# https://leetcode.com/problems/k-closest-points-to-origin/description/

# points= [[-2,-6],[-7,-2], [-8,1],[2,8], [-9,6],[10,3]]
# k=5

from typing import List

class Solution:
    def kClosestQuickSort(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calcDistance(point):
            return (point[0])**2 + (point[1])**2

        def quickSort(s, e):
            pivot = points[e]
            pivotDist = calcDistance(pivot)
            left = s
            for i in range(s, e):
                if calcDistance(points[i]) < pivotDist:
                    points[left], points[i] = points[i], points[left]
                    left += 1

            points[left], points[e] = points[e], points[left]

            if k <= left and left - 1 >= s:
                quickSort(s, left - 1)
            if k > left and left + 1 <= e:
                quickSort(left + 1, e)

        quickSort(0, len(points) - 1)
        return points[:k]

        def kClosestMinHeap(self, points: List[List[int]], k: int) -> List[List[int]]:
            minHeap = []

            distance = lambda x: x[0]**2 + x[1]**2 
            for point in points:
                minHeap.append([distance(point), point[0], point[1]])

            heapq.heapify(minHeap)

            res = []
            for i in range(k):
                lst = heapq.heappop(minHeap) # distance, x, y
                res.append(lst[1:])

            return res
