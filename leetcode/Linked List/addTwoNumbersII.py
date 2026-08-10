from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:

    def reverseList(self, l_n):
        curr_node = l_n
        prev_node = None

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        return prev_node


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        iter_l1 = reversed_l1 = self.reverseList(l1)
        iter_l2 = self.reverseList(l2)
        remainder = 0

        while iter_l1:
            val1 = 0
            val2 = 0
            if iter_l1: val1 = iter_l1.val
            if iter_l2: val2 = iter_l2.val
            sm = val1 + val2 + remainder
            remainder = sm // 10
            iter_l1.val = sm % 10

            if (remainder != 0 and not iter_l1.next) or (not iter_l1.next and iter_l2 and iter_l2.next):
                iter_l1.next = ListNode()

            iter_l1 = iter_l1.next
            if iter_l2: iter_l2 = iter_l2.next

        return self.reverseList(reversed_l1)
