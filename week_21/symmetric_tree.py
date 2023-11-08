from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_root = root.left
        right_root = root.right
        def helper(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            check_1 = helper(left.right, right.left)
            check_2 = helper(right.right, left.left)
            return check_1 and check_2
        return helper(left_root, right_root)
        