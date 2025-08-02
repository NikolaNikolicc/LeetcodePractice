from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, COLS - 1
        for r in range(ROWS // 2):
            for c in range(left, right):
                tmp = matrix[r][c]

                matrix[r][c] = matrix[ROWS - c - 1][left]

                matrix[ROWS - c - 1][left] = matrix[ROWS - r - 1][COLS - c - 1]

                matrix[ROWS - r - 1][COLS - c - 1] = matrix[c][right]

                matrix[c][right] = tmp

            print(matrix)
            right -= 1
            left += 1

matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol = Solution()
sol.rotate(matrix)