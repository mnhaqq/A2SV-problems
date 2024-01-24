from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0

        def traversal(node):
            nonlocal count
            if node:
                count += 1
            else:
                return
            traversal(node.left)
            traversal(node.right)
        traversal(root)
        return count