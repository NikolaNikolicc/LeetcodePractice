# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/

class Solution(object):

    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        cnt = Counter(students)
        retval = len(students)

        for sandwich in sandwiches:
            if cnt[sandwich] > 0:
                cnt[sandwich] -= 1
                retval -= 1
            else:
                return retval
        return retval