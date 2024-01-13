from typing import Optional
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        #build graph using dfs
        adj_list = defaultdict(list)

        def dfs(parent, node):
            if not node:
                return
            
            if parent:
                adj_list[node.val].append(parent.val)
            if node.left:
                adj_list[node.val].append(node.left.val)
                dfs(node, node.left)
            if node.right:
                adj_list[node.val].append(node.right.val)
                dfs(node, node.right)
        dfs(None, root)

        #find amount of time needed for tree to be infected
        queue = deque()
        queue.append(start)

        visited = set()
        level = -1

        while queue:
            len_level = len(queue)

            for _ in range(len_level):
                node = queue.popleft()
                visited.add(node)

                for nei in adj_list[node]:
                    if nei not in visited:
                        queue.append(nei)
            level += 1
        return level