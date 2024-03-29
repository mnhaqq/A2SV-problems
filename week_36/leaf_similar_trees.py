from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def traverse(node, arr):
            if not node:
                return
            if not node.left and not node.right:
                arr.append(node.val)
                return
            traverse(node.left, arr)
            traverse(node.right, arr)

        arr1 = []
        arr2 = []
        traverse(root1, arr1)
        traverse(root2, arr2)
        return arr1 == arr2