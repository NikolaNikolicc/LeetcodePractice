"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        
        copies = {}

        curr = head
        while curr:
            copyNode = Node(curr.val, None, None)
            copies[curr] = copyNode
            curr = curr.next

        curr = head
        while curr:
            if curr.next:
                copies[curr].next = copies[curr.next]
            if curr.random:
                copies[curr].random = copies[curr.random]
            curr = curr.next

        return copies[head]