from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        queue = [(root, -float("Inf"), +float("Inf"))]
        while queue:
            node = queue.pop(0)
            node_val, lower, upper = node
            if node_val.left:
                if lower < node_val.left.val < node_val.val:
                    queue.append((node_val.left, lower, node_val.val))
                else:
                    return False
            if node_val.right:
                if node_val.val < node_val.right.val < upper:
                    queue.append((node_val.right, node_val.val, upper))
                else:
                    return False
        return True




