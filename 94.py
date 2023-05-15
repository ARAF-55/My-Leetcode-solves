from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traversal(root_node):
            if root_node is None:
                return
            traversal(root_node.left)
            res.append(root_node.val)
            traversal(root_node.right)

        traversal(root)
        return res
