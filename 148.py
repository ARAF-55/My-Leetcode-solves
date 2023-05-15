from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_middle(self, node):
        slow, fast = node, node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        dummy_node = ListNode()
        temp = dummy_node
        while left and right:
            if left.val < right.val:
                temp.next = left
                left = left.next
                temp = temp.next
            else:
                temp.next = right
                right = right.next
                temp = temp.next
        if left:
            temp.next = left
        if right:
            temp.next = right
        return dummy_node.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left = head
        right = self.get_middle(left)
        temp = right.next
        right.next = None
        right = temp
        first_part = self.sortList(left)
        second_part = self.sortList(right)
        return self.merge(first_part, second_part)


dummy = ListNode()
linkedlist = ListNode(4)
dummy.next = linkedlist
linkedlist.next = ListNode(2)
linkedlist = linkedlist.next
linkedlist.next = ListNode(1)
linkedlist = linkedlist.next
linkedlist.next = ListNode(3)
linkedlist = linkedlist.next
linkedlist.next = ListNode(5)


solve = Solution()
the_list = solve.sortList(dummy.next)
while the_list:
    print(the_list.val)
    the_list = the_list.next
