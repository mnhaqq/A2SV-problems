from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        def helper(root):
            if not root:
                return
            arr.append(root.val)
            helper(root.left)
            helper(root.right)
        
        arr = []
        helper(root)
        return arr