from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            nonlocal ans
            if not node:
                return

            ans += str(node.val)
            if node.left or node.right:
                ans += "("
                dfs(node.left)
                ans += ")"

            if node.right:
                ans += "("
                dfs(node.right)
                ans += ")"

        
        ans = ""
        dfs(root)
        return ans