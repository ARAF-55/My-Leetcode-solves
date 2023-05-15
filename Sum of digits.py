from typing import Optional


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            column_sum = l1_val + l2_val + carry
            carry = column_sum // 10
            new_node = ListNode(column_sum % 10)
            current.next = new_node
            current = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


