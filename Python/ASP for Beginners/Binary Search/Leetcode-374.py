# https://leetcode.com/problems/guess-number-higher-or-lower/description/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        s, e = 1, n
        while s <= e:
            mid = (s + e) // 2

            res = guess(mid)
            if res == -1:
                e = mid - 1
            elif res == 1:
                s = mid + 1
            elif res == 0:
                return mid

    def guessNumberTernarySearch(self, n: int) -> int:
        l, r = 1, n
        while True:
            m1 = l + (r - l) // 3
            m2 = r - (r - l) // 3
            if guess(m1) == 0:
                return m1
            if guess(m2) == 0:
                return m2
            if guess(m1) + guess(m2) == 0:
                l = m1 + 1
                r = m2 - 1
            elif guess(m1) == -1:
                r = m1 - 1
            else:
                l = m2 + 1
        