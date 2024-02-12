from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            nonlocal ans, prev
            if not node:
                return

            inorder(node.left)
            if prev:
                ans = min(ans, abs(prev.val - node.val))
            prev = node
            inorder(node.right)
        
        prev = None
        ans = float('inf')
        inorder(root)
        return ans
        