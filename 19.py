from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r_node = ListNode(0)
        r_node.next = head
        while n > 0:
            r_node = r_node.next
            n -= 1
        l_node = ListNode(0)
        l_node.next = head
        temp = l_node
        while r_node.next:
            r_node = r_node.next
            temp = temp.next
        temp.next = temp.next.next
        return l_node.next
