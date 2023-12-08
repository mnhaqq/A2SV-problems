from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        queue = deque([root])
        ans = []

        while queue:
            curr_level = 0
            len_level = len(queue)
            for _ in range(len_level):
                node = queue.popleft()
                curr_level += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(curr_level/len_level)
        return ans