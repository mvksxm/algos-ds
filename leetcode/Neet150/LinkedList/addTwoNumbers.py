from typing import Optional

# n = max(len(l1), len(l2))
# TC -> O(n)
# SC -> O(1)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        iter_l1 = l1
        iter_l2 = l2
        carry = 0

        while iter_l1:

            num1 = iter_l1.val
            num2 = iter_l2.val if iter_l2 else 0
            sm = num1 + num2 + carry

            carry = sm // 10
            remainder = sm % 10

            iter_l1.val = remainder

            if not iter_l1.next and iter_l2 and iter_l2.next:
                iter_l1.next = ListNode()
            elif not iter_l1.next and carry:
                iter_l1.next = ListNode(carry)
                carry = 0

            if iter_l2: iter_l2 = iter_l2.next
            iter_l1 = iter_l1.next


        return l1