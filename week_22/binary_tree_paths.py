from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        def helper(c_root):
            nonlocal root
            if not c_root.left and not c_root.right:
                if c_root != root:
                    curr.append("->")
                curr.append(str(c_root.val))
                result.append("".join(curr))
                curr.pop()
                if c_root != root:
                    curr.pop()
                return
            if root == c_root:
                curr.append(str(c_root.val))
                if c_root.left:
                    helper(c_root.left)
                if c_root.right:
                    helper(c_root.right)
                curr.pop()
            else:
                curr.append("->")
                curr.append(str(c_root.val))
                if c_root.left:
                    helper(c_root.left)
                if c_root.right:
                    helper(c_root.right)
                curr.pop()
                curr.pop()

        result = []
        curr = []
        helper(root)
        return result