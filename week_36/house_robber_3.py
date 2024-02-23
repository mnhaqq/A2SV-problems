from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dp(node):
            if not node:
                return (0, 0)
            if not node.left and not node.right:
                return (node.val, 0)
            a = dp(node.left)
            b = dp(node.right)

            return (node.val + a[1] + b[1], max(a[0] + b[0], a[1] + b[1], a[1] + b[0], a[0] + b[1]))

        return max(dp(root))     


