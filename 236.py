class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root is p or root is q:
            return root
        search_left = self.lowestCommonAncestor(root.left, p, q)
        search_right = self.lowestCommonAncestor(root.right, p, q)
        if search_left and search_right:
            return root
        if search_left or search_right:
            if not search_left:
                return search_right
            return search_left
        return None
