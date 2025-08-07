from collections import deque, Counter
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def check(s,t):
            t = iter(t)
            return all(c in t for c in s)

        count = Counter(s)
        words = [c for c in count.keys() if count[c]>=k]
        words.sort()
        q = deque([''])
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                res = cur
                for c in words:
                    next = cur+c
                    if check(next*k,s):
                        q.append(next)
        return res
    
sol = Solution()
s = "letsleetcode"
k = 2
sol.longestSubsequenceRepeatedK(s, k)