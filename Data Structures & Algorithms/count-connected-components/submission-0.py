class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = set()
        count=0
        for s in range(len(adj)):
            if s not in visited:
                count += 1
                visited.add(s)
                q = [s]
                while q:
                    node = q.pop(0)
                    for i in adj[node]:
                        if i not in visited:
                            visited.add(i)
                            q.append(i)
        return count