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
        q = deque()
        q.append(src)
        visit.add(src)

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node == dst:
                    return True

                for n in self.adjList[node]:
                    if n not in visit:
                        q.append(n)
                        visit.add(n)

        return False

        
