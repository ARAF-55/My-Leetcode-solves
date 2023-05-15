from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque()
        queue.append([root])
        result = []
        odd = 0
        while queue:
            node = queue.popleft()
            next_node = []
            res_node = []
            while node:
                new_node = node.pop(0)
                res_node.append(new_node.val)
                if new_node.left:
                    next_node.append(new_node.left)
                if new_node.right:
                    next_node.append(new_node.right)
            if next_node:
                queue.append(next_node)
            if odd:
                res_node.reverse()
                result.append(res_node)
                odd = 0
            else:
                result.append(res_node)
                odd = 1
        return result
