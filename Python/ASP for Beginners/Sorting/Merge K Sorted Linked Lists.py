

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# [[1,2,4],[1,3,5],[3,6]]

# 3, 4, 6, 2, 31
# 7, 13, 15, 46
# 3 * 5 + 4 * 4 + 6 * 3 + 2 * 2 + 31 * 1
# minNode = 0

class Solution:    
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None
        return self.divide(lists, 0, len(lists) - 1)

    def divide(self, lists, l, r):
        if l > r:
            return None

        if l == r:
            return lists[l]

        mid = l + (r - l)//2
        left = self.divide(lists, l, mid)
        right = self.divide(lists, mid + 1, r)

        return self.conquer(left, right)

    def conquer(self, l, r):
        head = curr = ListNode()
        while l and r:
            if l.val < r.val:
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next
            curr = curr.next

        if l:
            curr.next = l
        if r:
            curr.next = r

        return head.next
