class ListNode():
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

class BrowserHistory(object):

    def __init__(self, homepage):
        self.current = ListNode(homepage)

    # 0<->1<->2<->3
    def visit(self, url):
        if self.current.next:
            self.current.next.prev = None
        newNode = ListNode(url)
        self.current.next = newNode
        newNode.prev = self.current
        self.current = self.current.next

    def back(self, steps):
        while steps > 0 and self.current.prev:
            steps -= 1
            self.current = self.current.prev
        return self.current.val       

    def forward(self, steps):
        while steps > 0 and self.current.next:
            steps -= 1
            self.current = self.current.next
        return self.current.val  
        


# Your BrowserHistory object will be instantiated and called as such:
homepage = "leetcode.com"
obj = BrowserHistory(homepage)
url = "google.com"
obj.visit(url)
steps = 5
param_2 = obj.back(steps)
param_3 = obj.forward(steps)