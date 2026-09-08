class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = [i for i in range(n + 1)]

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa == pb:
                return False
            parent[pa] = pb
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]