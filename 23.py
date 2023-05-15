from typing import List, Optional, Any


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, list1, list2):
        res = ListNode()
        temp = res
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                temp = temp.next
                list1 = list1.next
            else:
                temp.next = list2
                temp = temp.next
                list2 = list2.next
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2
        return res.next

    def mergeKLists(self, lists: List[Optional[ListNode]]):
        if not lists or len(lists) == 0:
            return None
        l, r = 0, len(lists) - 1
        if l < r:
            m = ((l + r) // 2)
            temp_1 = self.mergeKLists(lists[l:m + 1])
            temp_2 = self.mergeKLists(lists[m + 1:r + 1])
            temp_3 = self.merge(temp_1, temp_2)
            return temp_3
        else:
            return lists[l]
