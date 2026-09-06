class Solution:
    def islandsAndTreasure(self, grid):
        m, n = len(grid), len(grid[0])
        visited = {}
        q = []
        direc = [(1,0),(0,1),(-1,0),(0,-1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited[(i, j)] = True

        level = 0
        while q:
            for i in range(len(q)):
                r, c = q.pop(0)
                grid[r][c] = level
                for dr, dc in direc:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m) and (0 <= nc < n) and ((nr, nc) not in visited) and (grid[nr][nc] == 2147483647):
                        visited[(nr, nc)] = True
                        q.append((nr, nc))
            level += 1