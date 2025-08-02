class Solution(object):

    # O(k*n!/((n-k)!k!))
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        combinations = []
        combination = []

        def dfs(position):
            if len(combination) == k:
                combinations.append(combination[:])
                return 
            if position == n + 1:
                return

            for i in range(position, n + 1):
                combination.append(i)
                dfs(i + 1)
                combination.pop()
        
        dfs(1)
        return combinations
    
    # O(k*n^2)
    def combineWorseTimeComplexity(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        combinations = []
        combination = []

        def dfs(position):
            if len(combination) == k:
                combinations.append(combination[:])
                return 
            if position == n + 1:
                return

            combination.append(position)
            dfs(position + 1)
            combination.pop()

            dfs(position + 1)
        
        dfs(1)
        return combinations

sol = Solution()
n = 5
k = 2
print(sol.combine(k = k, n = n))
