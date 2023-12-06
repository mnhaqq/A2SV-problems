
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node, caller):
            if not node:
                return caller
            if node in visited:
                caller.neighbors.append(dic[node.val])
                return caller
            visited.add(node)
            new_node = Node(node.val)
            dic[new_node.val] = new_node
            if caller:
                caller.neighbors.append(new_node)

            for nei in node.neighbors:
                dfs(nei, new_node)
            return new_node


        visited = set()
        dic = dict()
        return dfs(node, None)
