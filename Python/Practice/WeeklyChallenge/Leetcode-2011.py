class Solution(object):
    def finalValueAfterOperationsOne(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        for op in operations:
            x += 44 - ord(op[1])

        return x
    
    def finalValueAfterOperationsTwo(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        for op in operations:
            if op[1] == "+":
                x += 1
            else:
                x -=1

        return x