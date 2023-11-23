from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal count
            nonlocal tmp
            if not root:
                return
            if not root.left and not root.right:
                count = min(tmp+1, count)
                return
            tmp += 1
            dfs(root.left)
            dfs(root.right)
            tmp -= 1

        count = float('inf')
        tmp = 0
        if not root:
            return 0
        dfs(root)
        return count
