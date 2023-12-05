from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        def dfs(root, path_sum):
            if not root:
                return
            if not root.left and not root.right:
                path_sum += root.val
                if path_sum == targetSum:
                    arr.append(root.val)
                    ans.append(arr[:])
                    arr.pop()
                return
        
            arr.append(root.val)
            dfs(root.left, path_sum + root.val)
            dfs(root.right, path_sum + root.val)
            arr.pop()
        
        ans = []
        arr = []
        dfs(root, 0)
        return ans