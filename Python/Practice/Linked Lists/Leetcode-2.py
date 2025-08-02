from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SolutionNeetcode:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = start = ListNode()
        carry = 0
        while l1 or l2 or carry:
            num = carry

            if not l1 and not l2:
                pass
            elif not l1:
                num += l2.val
                l2 = l2.next
            elif not l2:
                num += l1.val
                l1 = l1.next
            else:
                num += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next

            dummy.next = ListNode(num % 10) 
            dummy = dummy.next
            carry = num // 10
            
        return start.next
            