from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        ans = []
        queue = deque()
        if root:
            queue.append(root)

        order = 0
        while queue:
            level = len(queue)
            level_nodes = []

            for i in range(level):
                node = queue.popleft()
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level_nodes)
        return ans[::-1]