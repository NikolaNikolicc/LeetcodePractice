from typing import List
import heapq
import collections

class Solution:
    def leastIntervalNeetcode(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = collections.deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
    
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cache = {i: 0 for i in range(ord("Z") - ord("A") + 1)}
        
        for task in tasks:
            cache[ord(task) - ord("A")] += 1

        maxHeap = []

        for key, elem in cache.items():
            if elem > 0:
                maxHeap.append((-elem, key))

        heapq.heapify(maxHeap)
        interval = 0
        print(maxHeap)

        queue = collections.deque()

        while queue or maxHeap:
            if not maxHeap and queue and interval - queue[0][0] <= n:
                interval += 1
                continue
            
            if queue and interval - queue[0][0] > n and \
                (not maxHeap or (maxHeap and cache[queue[0][1]] >= cache[maxHeap[0][1]])):
                lastUsed, key = queue.popleft()
            else:
                tmp = heapq.heappop(maxHeap)
                elem = -tmp[0]
                key = tmp[1]
            cache[key] -= 1
            if cache[key] > 0:
                queue.append((interval, key)) 

            print(" after interval: " + str(interval) + " maxHeap: " + str(maxHeap) + "queue: " + str(queue))
            interval += 1

        return interval
    
sol = Solution()
tasks=["A","A","A","B","B","B","C","C","C","D","D","E"]
n=2
print(sol.leastInterval(tasks, n))
