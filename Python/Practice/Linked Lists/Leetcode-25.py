# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        head = ListNode(0, head)

        size = 0
        curr = head.next
        while curr:
            curr = curr.next
            size += 1

        iteration = 0
        end = None
        curr = head.next
        
        while curr:
            if iteration * k + k <= size:
                i = 0
                prev = None
                tmp = None
                start = curr
                while i < k and curr:
                    tmp = curr
                    curr = curr.next
                    tmp.next = prev
                    prev = tmp
                    i += 1

                if not end:
                    end = head.next
                    head.next = tmp
                else:
                    end.next = tmp
                    end = start

                iteration += 1
            else:
                if end:
                    end.next = curr
                
                return head.next

        return head.next