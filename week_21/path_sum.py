from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root):
            nonlocal check
            if not root:
                return
            check += root.val
            if not root.left and not root.right:
                ans = check == targetSum
                check -= root.val
                return ans
            left = helper(root.left)
            right = helper(root.right)
            check -= root.val
            return left or right

        check = 0
        if not root:
            return False
        return helper(root)