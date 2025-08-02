class Solution(object):
    def uniquePathsWithObstaclesTwoArrays(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        oldRow = [0]*len(obstacleGrid[0])
        oldRow[-1] = 1

        for r in range(len(obstacleGrid) - 1, -1, -1):
            newRow = [0]*len(obstacleGrid[0])
            
            for c in range(len(obstacleGrid[0]) - 1, -1, -1):
                if obstacleGrid[r][c] != 1:
                    if c + 1 < len(obstacleGrid[0]):
                        newRow[c] = oldRow[c] + newRow[c + 1]
                    else:
                        newRow[c] = oldRow[c]

            oldRow = newRow[:] 
        return oldRow[0]

    def uniquePathsWithObstacles(self, obstacleGrid):
        oldRow = [0]*len(obstacleGrid[0])
        oldRow[-1] = 1

        for r in range(len(obstacleGrid) - 1, -1, -1):
            for c in range(len(obstacleGrid[0]) - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    oldRow[c] = 0
                elif c + 1 < len(obstacleGrid[0]):
                    oldRow[c] = oldRow[c] + oldRow[c + 1]
                
        return oldRow[0]