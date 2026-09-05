"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if node is None:
            return None

        newNode = {}

        def dfs(node):
            if node in newNode:
                return newNode[node]

            cnode = Node(node.val)
            newNode[node] = cnode

            for n in node.neighbors:
                cnode.neighbors.append(dfs(n))

            return cnode

        return dfs(node)