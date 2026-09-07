class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adj = [[] for i in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)

        Visited = {}
        dfsVi = {}

        def dfs(node):
            Visited[node] = True
            dfsVi[node] = True
            for nei in adj[node]:
                if nei in dfsVi and dfsVi[nei] :
                    return True
                if nei not in Visited:
                    if dfs(nei):
                        return True
            dfsVi[node] = False
            return False

        for i in range(numCourses):
            if i not in Visited:
                if dfs(i):
                    return False
        return True