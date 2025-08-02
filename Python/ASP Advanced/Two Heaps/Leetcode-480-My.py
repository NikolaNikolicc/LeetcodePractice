import heapq

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        minHeap = []
        maxHeap = []
        
        def add(val):
            heapq.heappush(maxHeap, -val)

            if minHeap and minHeap[0] < -maxHeap[0]:
                val = -heapq.heappop(maxHeap)
                heapq.heappush(minHeap, val)
            while len(minHeap) - len(maxHeap) > 1:
                val = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -val)
            while len(maxHeap) - len(minHeap) > 1:
                val = -heapq.heappop(maxHeap)
                heapq.heappush(minHeap, val)

        def findMid():
            if not minHeap and not maxHeap:
                return -1
            
            if len(minHeap) > len(maxHeap):
                return minHeap[0]

            if len(maxHeap) > len(minHeap):
                return -maxHeap[0]

            return float(minHeap[0] - maxHeap[0]) / 2

        outputList = []
        def addMid():
            mid = findMid()
            outputList.append(mid)

        for i in range(k):
            add(nums[i])

        addMid()

        print(minHeap)
        print(maxHeap)
        print("----------------------------------")


        l = 0
        for i in range(k, len(nums)):
            
            tmp = []

            if maxHeap and nums[l] <= -maxHeap[0]:
                while maxHeap and nums[l] <= -maxHeap[0]:
                    val = -heapq.heappop(maxHeap)
                    if val != nums[l]:
                        tmp.append(val)
                    else:
                        break
            elif minHeap and nums[l] >= minHeap[0]:
                while minHeap and nums[l] >= minHeap[0]:
                    val = heapq.heappop(minHeap)
                    if val != nums[l]:
                        tmp.append(val)
                    else:
                        break

            while tmp != []:
                val = tmp.pop()
                add(val)

            add(nums[i])
            print(minHeap)
            print(maxHeap)
            addMid()
            print("----------------------------------")
            l += 1

        return outputList


sol = Solution()
nums = [7,0,3,9,9,9,1,7,2,3]
k = 6
sol.medianSlidingWindow(nums, k)


# time limit exceeded