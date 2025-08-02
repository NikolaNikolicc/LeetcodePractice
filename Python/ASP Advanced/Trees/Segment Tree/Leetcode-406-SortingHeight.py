from typing import List

class Solution:

    # the  idea is to count every element that is bigger or equal to the current element (cnt pointer), wwe are counting only [] because if p[i] != [] it means element is lower than current (can't be equal because we firstly set position of element with higher number of greater or equal nodes)
    def reconstructQueueAscending(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        people.sort(key=lambda x: (x[0], -x[1]))
        res = [[] for _ in range(n)]
        print(people)
        for p in people:
            cnt = i = 0
            while i < n:
                if not res[i]:
                    if cnt == p[1]:
                        break
                    cnt += 1
                i += 1
            res[i] = p
            
        return res

    def reconstructQueueDescending(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        print(people)
        people.sort(key=lambda x: (-x[0], x[1]))
        for p in people:
            res.insert(p[1], p)
            print(res)
        return res

sol = Solution()
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(sol.reconstructQueueAscending(people))