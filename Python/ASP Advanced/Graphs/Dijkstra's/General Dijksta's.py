class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjBook = {i:[] for i in range(n)}

        for edge in edges:
            adjBook[edge[0]].append((edge[1], edge[2]))

        print(adjBook)
        shortest = {i: -1 for i in range(n)}
        minHeap = [(0, src)]

        while minHeap:

            w1, src = heapq.heappop(minHeap)
            # print("src: " + str(src) + " w1: " + str(w1))
            if shortest[src] != -1:
                continue


            shortest[src] = w1

            for dst, w2 in adjBook[src]:
                if shortest[dst] == -1:
                    heapq.heappush(minHeap, (w1 + w2, dst))

        return shortest