class Graph:
    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = set()
        if dst not in self.adjList:
            self.adjList[dst] = set()

        self.adjList[src].add(dst)
        
    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjList:
            return False
        if dst in self.adjList[src]:
            self.adjList[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()

        def dfs(node):
            if node == dst:
                return True
            if node in visit:
                return False

            visit.add(node)
            hasPath = False
            for n in self.adjList[node]:
                hasPath = hasPath or dfs(n)
            visit.remove(node)
            return hasPath

        return dfs(src)
