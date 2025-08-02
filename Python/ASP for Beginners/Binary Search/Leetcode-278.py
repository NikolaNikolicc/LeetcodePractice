# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


# 1 2 3 4 5 | 6 7 8
# false, s = 5, mid = 4
# true, bad = 6, mid = 6, end = 5
# false, s = 6

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        bad = n

        s, e = 1, n - 1

        while s <= e:

            mid = (s + e) // 2
            if isBadVersion(mid):
                bad = mid
                e = mid - 1
            else:
                s = mid + 1
        return bad
