from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, parent, direction):
            if not node:
                return

            dfs(node.left, node, 'left')
            dfs(node.right, node, 'right')

            if not node.left and not node.right and node.val == 0:
                if direction == 'left':
                    parent.left = None
                elif direction == 'right':
                    parent.right = None
        
        dummy = TreeNode(0, root)
        dfs(root, dummy, 'left')
        return dummy.left