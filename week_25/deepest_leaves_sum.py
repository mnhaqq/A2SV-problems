from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            nonlocal max_depth
            nonlocal ans
            if not root:
                return
            if depth > max_depth:
                max_depth = depth
                ans = 0
            if depth == max_depth:
                ans += root.val
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        
        ans = 0
        max_depth = float("-inf")
        dfs(root, 0)
        return ans