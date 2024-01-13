from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
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
        

        #find nodes distance k away using bfs
        queue = deque()
        queue.append(target.val)

        visited = set()
        level = 0
        ans = []

        while queue:
            len_level = len(queue)

            if level == k:
                while queue:
                    ans.append(queue.popleft())
                break

            for _ in range(len_level):
                node = queue.popleft()
                visited.add(node)

                for nei in adj_list[node]:
                    if nei not in visited:
                        queue.append(nei)
            level += 1
        return ans