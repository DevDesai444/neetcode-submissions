class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        adj = [[] for i in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)
        visited = {}
        dfsVi = {}
        stack = []
        hasCycle = [False]

        def dfs(node):
            visited[node] = True
            dfsVi[node] = True
            for i in adj[node]:
                if (i in dfsVi) and dfsVi[i]:
                    hasCycle[0] = True
                    return
                if i not in visited:
                    dfs(i)
            dfsVi[node] = False
            stack.append(node)

        for i in range(numCourses):
            if i not in visited:
                dfs(i)

        if hasCycle[0]:
            return []
        else:
            ans = []
            for i in range(len(stack)):
                ans.append(stack.pop())
            return ans