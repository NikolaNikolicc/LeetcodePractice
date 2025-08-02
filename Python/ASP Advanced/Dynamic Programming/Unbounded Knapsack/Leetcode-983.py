class Solution(object):

    def mincostTickets(self, days, costs):
        dp = [0]*(len(days) + 1)

        for d in range(len(days)-1, -1, -1):
            j = d
            dp[d] = float("inf")
            for cost, duration in zip(costs, [1, 7, 30]):
                while j < len(days) and days[j] < days[d] + duration:
                    j += 1
                dp[d] = min(dp[d], cost + dp[j])
        return dp[0]

    def mincostTicketsCacheing(self, days, costs):
        dp = {}

        def dfs(i):

            if i == len(days):
                return 0
            
            if i in dp:
                return dp[i]

            j = i
            ret = float("inf")
            for cost, duration in zip(costs, [1, 7, 30]):
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1

                ret = min(ret, dfs(j) + cost)
            dp[i] = ret
            return ret

        return dfs(0)
    
    
    def mincostTicketsMemoization(self, days, costs):
        dp = {}
        def dfs(day, remaining, spent):
            if (day, remaining, spent) in dp:
                return dp[(day, remaining, spent)]
            if day == len(days) - 1:
                if remaining > 0:
                    return spent
                return spent + min(costs)

            dayDiff = days[day + 1] - days[day]
            if remaining > 0:
                return dfs(day + 1, remaining - dayDiff, spent)
            
            dp[(day, remaining, spent)] = min(
            dfs(day + 1, 1 - dayDiff, spent + costs[0]),
            dfs(day + 1, 7 - dayDiff, spent + costs[1]),
            dfs(day + 1, 30 - dayDiff, spent + costs[2])
            )
            return dp[(day, remaining, spent)]

        return dfs(0, 0, 0)

days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
sol = Solution()
print(sol.mincostTickets(days, costs))