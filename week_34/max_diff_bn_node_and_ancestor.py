from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, min_val, max_val):
            nonlocal ans
            ans = max(ans, abs(node.val - min_val))
            ans = max(ans, abs(node.val - max_val))

            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)

            if node.left:
                dfs(node.left, min_val, max_val)
            if node.right:
                dfs(node.right, min_val, max_val)


        ans = 0
        dfs(root, root.val, root.val)
        return ans