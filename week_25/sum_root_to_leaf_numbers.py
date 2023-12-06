from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal ans
            if not root:
                return
            if not root.left and not root.right:
                arr.append(str(root.val))
                tmp = arr[:]
                tmp = "".join(tmp)
                ans += int(tmp)
                arr.pop()
                return
            
            arr.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            arr.pop()
        
        ans = 0
        arr = []
        dfs(root)
        return ans