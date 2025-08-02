# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseListRecursively(self, head):
        if not head:
            return None
        
        node = head
        if head.next:
            node = self.reverseListRecursively(head.next)
            head.next.next = head
        head.next = None

        return node

    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        prev, curr = head, head.next
        nxt = curr.next if curr else None
        prev.next = None
        while(curr):
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next if nxt else None
        return prev

