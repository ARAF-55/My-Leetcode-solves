from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.optimum_value = -float("inf")

    def maxPathSum(self, root: TreeNode) -> int:

        def the_path(node, the_cache):
            if node in the_cache:
                return the_cache[node]
            if not node:
                return 0
            left_val = the_path(node.left, the_cache)
            right_val = the_path(node.right, the_cache)
            node_val = node.val + max(left_val, 0) + max(right_val, 0)
            self.optimum_value = max(self.optimum_value, node_val)
            the_cache[node] = node.val + max(0, left_val, right_val)
            return node.val + max(0, left_val, right_val)

        the_path(root, {})
        return self.optimum_value
