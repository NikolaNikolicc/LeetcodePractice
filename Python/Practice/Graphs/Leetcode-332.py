class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = defaultdict(list)
        tickets.sort()

        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]
        def dfs(airport):

            if len(res) == len(tickets) + 1:
                return True

            if airport not in adj:
                return False
            
            to = list(adj[airport])
            for i in range(len(to)):

                res.append(to[i])
                adj[airport].pop(i)

                if dfs(to[i]):
                    return True

                adj[airport].insert(i, to[i])
                res.pop()
            return False

        dfs("JFK")
        return res