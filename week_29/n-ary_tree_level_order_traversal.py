from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        ans = []
        queue = deque()

        if root:
            queue.append(root)
        
        while queue:
            level = len(queue)
            level_nodes = []

            for i in range(level):
                node = queue.popleft()
                level_nodes.append(node.val)

                for child in node.children:
                    queue.append(child)
            ans.append(level_nodes)
        return ans