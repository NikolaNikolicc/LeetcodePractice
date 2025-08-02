class Node:
    def __init__(self, startTime, endTime):
        self.startTime = startTime
        self.endTime = endTime
        self.left = None
        self.right = None


class MyCalendar(object):

    def __init__(self):
        self.root = None

    def book(self, startTime, endTime):

        def insert(root):
            if not self.root:
                self.root = Node(startTime, endTime)
                return True
            if startTime >= root.endTime:
                if not root.left:
                    root.left = Node(startTime, endTime)
                    return True
                return insert(root.left)
            if endTime <= root.startTime:
                if not root.right:
                    root.right = Node(startTime, endTime)
                    return True
                return insert(root.right)
            return False

        return insert(self.root)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)