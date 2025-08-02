class Solution:
    def hammingWeightBitMask(self, n: int) -> int:
        cnt = 0
        for i in range(32):
            if n & (1 << i):
                cnt += 1
        return cnt

    def hammingWeight(self, n):
        cnt = 0
        while n > 0:
            if n & 1:
                cnt += 1
            n >>= 1
        return cnt

    # in this solution we efficiently skipping all zeroes
    def hammingWeightOptimal(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res