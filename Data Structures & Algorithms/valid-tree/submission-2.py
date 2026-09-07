class Solution:
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set([0])
        stack = [0]
        while stack:
            node = stack.pop()
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)

        return len(visited) == n