from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        one = Counter(s1)
        s1s = len(s1)

        two = defaultdict(int)
        size = 0
        l = 0
        for r in range(len(s2)):
            
            if s2[r] in one and two[s2[r]] < one[s2[r]]:
                size += 1
                
            two[s2[r]] += 1

            if s2[r] not in one:
                size = 0
                l = r + 1
                two = defaultdict(int)
                continue

            if r - l + 1 > s1s:
                if s2[l] in one and two[s2[l]] <= one[s2[l]]:
                    size -= 1
                two[s2[l]] -= 1
                l += 1

            if size == s1s:
                return True

        return False
