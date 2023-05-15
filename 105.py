from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder == [] or inorder == []:
            return None
        root = TreeNode(preorder[0])
        left_tree_bound = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:left_tree_bound + 1], inorder[:left_tree_bound])
        root.right = self.buildTree(preorder[left_tree_bound+1:], inorder[left_tree_bound+1:])
        return root
