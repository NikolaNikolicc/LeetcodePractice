# https://leetcode.com/problems/implement-stack-using-queues/description/

'''
Questions

1) In case that we have empty stack what we wwawnt to remove in pop and top operations?

'''

class MyStack(object):

    def __init__(self):
        self.queue = []

    # [3, 0, 1, 2, 4]
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if not len(self.queue):
            return -1
        
        for i in range(len(self.queue) - 1):
            elem = self.queue.pop(0)
            self.queue.append(elem)
        return self.queue.pop(0)
        
        

    def top(self):
        """
        :rtype: int
        """
        if not len(self.queue):
            return -1
        
        for i in range(len(self.queue) - 1):
            elem = self.queue.pop(0)
            self.queue.append(elem)
        elem = self.queue.pop(0)
        self.queue.append(elem)
        return elem
        

    def empty(self):
        """
        :rtype: bool
        """
        return False if len(self.queue) > 0 else True


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
x = 1
obj.push(x)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()