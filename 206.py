from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node, prev):
            if not node:
                return prev
            temp = node.next
            node.next = prev
            prev_node = node
            return reverse(temp, prev_node)

        return reverse(head, None)
