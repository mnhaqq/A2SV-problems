# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()

        queue.append(root)

        i = 0
        while queue:
            level = len(queue)
            prev = None
            for _ in range(level):
                node = queue.popleft()
                if ((i % 2 == 0) and (node.val % 2 == 0 or (prev and prev.val >= node.val))) or \
                    ((i % 2 != 0) and (node.val % 2 != 0 or (prev and prev.val <= node.val))):
                    return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                prev = node

            i += 1
        return True
