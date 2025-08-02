from typing import List
import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # v = s/t ->  t = s/v
        remaining = [(position[i], (target - position[i])/speed[i]) for i in range(len(position))]
        remaining.sort(key = lambda i: i[0])
        # print(remaining)

        stack = []
        groups = 0
        for i in range(len(remaining) - 1, -1, -1):
            skip = 0
            while stack and stack[-1] < remaining[i][1]:
                stack.pop()
                skip += 1

            if skip or not stack:
                groups += 1
                stack.append(remaining[i][1])

            # print("stack: " + str(stack) + " groups: " + str(groups))
        return groups

sol = Solution()
target=10
position=[8,3,7,4,6,5]
speed=[4,4,4,4,4,4]
print(sol.carFleet(target, position, speed))