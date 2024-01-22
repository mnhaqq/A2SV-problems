from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque()
        if root:
            queue.append(root)

        while queue:
            len_level = len(queue)
            num_nodes = len_level
            for _ in range(len_level):
                node = queue.popleft()
                num_nodes -= 1
                if queue and num_nodes > 0:
                    node.next = queue[0]
                else:
                    node.next = None
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                
        return root
        