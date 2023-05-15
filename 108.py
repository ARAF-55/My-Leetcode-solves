from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def the_tree(l, r):
            if l > r:
                return None
            middle = (l + r) // 2
            root_node = TreeNode(nums[middle])
            root_node.left = the_tree(l, middle - 1)
            root_node.right = the_tree(middle + 1, r)
            return root_node

        root = the_tree(0, len(nums)-1)
        return root
