class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
  
        used = [False]*len(capital)
        profit = w
        for i in range(k):
            maxProfit= float("-inf")
            position = -1

            for c in range(len(capital)):
                if capital[c] <= profit and not used[c] and profits[c] > maxProfit:
                    maxProfit = profits[c]
                    position = c

            if position != -1:
                used[position] = True
                profit += maxProfit
            print(position)

        return profit

# time limit exceeded