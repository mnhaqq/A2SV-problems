
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root, check):
            nonlocal ans
            if not root:
                return
            if not root.children:
                ans = max(ans, check)
                return
            for child in root.children:
                dfs(child, check + 1)
        
        ans = 0
        dfs(root, 1)
        return ans