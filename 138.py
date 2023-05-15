class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        temp = head
        hash_map = {}
        while temp:
            new_node = Node(temp.val)
            hash_map[temp] = new_node
            temp = temp.next
        temp = head
        while temp:
            if temp.next is None:
                hash_map[temp].next = None
            else:
                hash_map[temp].next = hash_map[temp.next]
            if temp.random is None:
                hash_map[temp].random = None
            else:
                hash_map[temp].random = hash_map[temp.random]
            temp = temp.next
        return hash_map[head]
