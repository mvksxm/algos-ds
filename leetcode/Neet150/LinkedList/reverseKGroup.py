from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Approach: perform while loop iteration. Reverse each group with len k by using a recursive call and connect it to
# the previous group. Head returned from the recursive call put as the next node after current iteration tail and tail returned
# from the recursive call -> becomes current iteration tail.
# TC -> O(n); n -> amount of nodes in a list
# SC -> O(k); k -> group length

class Solution:

    # Recursive approach
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def recurseReverse(curr_node, curr_k):

            # Should return new head and tail
            if curr_k == k:
                return curr_node, curr_node, True

            if not curr_node.next:
                return curr_node, None, False

            new_tail, new_head, status = recurseReverse(curr_node.next, curr_k + 1)
            if not status:
                return new_tail, curr_node, False

            curr_node.next = new_tail.next
            new_tail.next = curr_node
            return curr_node, new_head, True


        f_node = None
        i_node = None
        while True:
            curr_node = i_node.next if i_node else head
            n_tail, n_head, status = recurseReverse(curr_node, 1)
            if not f_node:
                f_node = n_head
            else:
                i_node.next = n_head

            if not n_tail.next: break
            i_node = n_tail

        return f_node
    