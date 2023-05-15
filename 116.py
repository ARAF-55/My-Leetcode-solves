from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return []
        queue = deque()
        queue.append(root)
        while queue:
            the_level_size = len(queue)
            for i in range(the_level_size):
                node = queue.popleft()
                if i != the_level_size - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)
        return root

