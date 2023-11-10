from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, low, high):
            if not root:
                return True
            elif root.val > low and root.val < high:
                ans = True
            else:
                ans = False
            left = helper(root.left, low, root.val)
            right = helper(root.right, root.val, high)
            return ans and left and right

        return helper(root, float("-inf"), float("inf"))