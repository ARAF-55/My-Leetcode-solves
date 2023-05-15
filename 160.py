from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempA, tempB = headA, headB
        dummyA, dummyB = tempA, tempB
        lenA = lenB = 0
        while dummyA:
            lenA += 1
            dummyA = dummyA.next
        while dummyB:
            lenB += 1
            dummyB = dummyB.next
        if lenA == 0 or lenB == 0:
            return None
        elif lenA >= lenB:
            while tempA:
                if lenA == lenB:
                    if tempA == tempB:
                        return tempA
                    tempA = tempA.next
                    tempB = tempB.next
                else:
                    tempA = tempA.next
                    lenA -= 1
            return tempA
        else:
            while tempB:
                if lenA == lenB:
                    if tempA == tempB:
                        return tempA
                    tempA = tempA.next
                    tempB = tempB.next
                else:
                    tempB = tempB.next
                    lenB -= 1
            return tempB




