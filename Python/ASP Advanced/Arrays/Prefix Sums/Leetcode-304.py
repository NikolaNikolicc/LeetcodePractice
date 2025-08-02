# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix(object):

    def __init__(self, matrix):

        ROWS, COLS = len(matrix), len(matrix[0])
        
        self.prefix = []
        
        lst = [0]*COLS
        for r in range(ROWS):
            total = 0
            for c in range(COLS):
                total += matrix[r][c]
                lst[c] = lst[c] + total
            self.prefix.append(lst[:])
        

    def sumRegion(self, row1, col1, row2, col2):

        total = self.prefix[row2][col2]
        if col1 > 0:
            total -= self.prefix[row2][col1 - 1]
        if row1 > 0:
            total -= self.prefix[row1 - 1][col2]
        if col1 > 0 and row1 > 0:
            total += self.prefix[row1 - 1][col1 - 1]
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)