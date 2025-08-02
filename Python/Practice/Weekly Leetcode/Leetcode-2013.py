from collections import defaultdict

class DetectSquares(object):

    def __init__(self):
        self.points = defaultdict(int)
        self.maxx = -1
        self.maxy = -1

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        self.points[(point[0], point[1])] += 1
        self.maxx = max(self.maxx, point[0])
        self.maxy = max(self.maxy, point[1])
        
    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        directions = [[-1, -1], [+1, -1], [+1, +1], [-1, +1]]
        px, py = point[0], point[1]
        count = 0
        for dir in directions:
            dx, dy = dir[0], dir[1]
            x, y = point[0] + dx, point[1] + dy

            while 0 <= x <= max(px, self.maxx) and 0 <= y <= max(py, self.maxy):
                multipl = 0
                if (x, y) in self.points and (x, py) in self.points and (px, y) in self.points:
                    multipl = self.points[(x, y)] * self.points[(x, py)] * self.points[(px, y)]

                count += multipl

                x = x + dx
                y = y + dy

        return count

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)