from typing import List
from collections import defaultdict

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        mp = defaultdict(list)

        for p in people:
            mp[p[1]].append(p[0])

        print(mp)
        for key in mp:
            mp[key].sort(reverse=True)

        print(mp)

        res = [] # res = [[5, 0], [7, 0]]
        for i in range(n): # n = 6
            # i = 3
            mini = -1 # mini = 0
            for k in mp:
                # k = 1
                if k > i:
                    continue
                cnt = 0
                # cnt = 0
                j = len(res) - 1
                while j >= 0:
                    # j = 1
                    if res[j][0] >= mp[k][-1]:
                        cnt += 1
                    j -= 1
                if cnt == k and (mini == -1 or mp[k][-1] < mp[mini][-1]):
                    mini = k

            res.append([mp[mini].pop(), mini])
            if not mp[mini]:
                mp.pop(mini)
        return res

sol = Solution()
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
sol.reconstructQueue(people)


# time limit exceeded