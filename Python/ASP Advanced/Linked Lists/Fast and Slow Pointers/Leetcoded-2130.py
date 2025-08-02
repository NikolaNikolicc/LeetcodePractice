# list:    2 4 6 2 4 2 3 5
# indices: 0 1 2 3 4 5 6 7
# twins:   7 6 5 4

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def pairSumExtraSpace(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        if not head:
            return 0
        
        mid, fast = head, head

        sums = collections.deque()
        while fast and fast.next:
            sums.append(mid.val)
            mid = mid.next
            fast = fast.next.next

        maxSum = float("-inf")
        
        while mid:
            val = sums.pop()
            maxSum = max(maxSum, val + mid.val)
            mid = mid.next
            
        return maxSum

    def pairSumReverseHalfLinkedList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        if not head:
            return 0
        
        prev, mid, fast = None, head, head

        while fast and fast.next:
            fast = fast.next.next
            tmp = mid.next
            mid.next = prev
            prev = mid
            mid = tmp

        maxSum = float("-inf")
        
        while mid:
            maxSum = max(maxSum, prev.val + mid.val)
            mid = mid.next
            prev = prev.next
            
        return maxSum