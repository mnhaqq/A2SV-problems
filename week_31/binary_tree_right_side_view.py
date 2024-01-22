from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        ans = []

        queue = deque()
        if root:
            queue.append(root)
        
        while queue:
            len_level = len(queue)
            ans.append(queue[-1].val)

            for _ in range(len_level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return ans