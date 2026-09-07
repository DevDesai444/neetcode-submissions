class Solution:
    def pacificAtlantic(self, grid):
        qp, qa, vp, va = [], [], set(), set()
        for j in range(len(grid[0])):
            qp.append((0, j))
            vp.add((0, j))
        for i in range(len(grid)):
            qp.append((i, 0))
            vp.add((i, 0))
        for j in range(len(grid[0])):
            qa.append((len(grid) - 1, j))
            va.add((len(grid) - 1, j))
        for i in range(len(grid)):
            qa.append((i, len(grid[0]) - 1))
            va.add((i, len(grid[0]) - 1))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(q, v):
            while q:
                for _ in range(len(q)):
                    r, c = q.pop(0)
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in v and grid[nr][nc] >= grid[r][c]:
                            v.add((nr, nc))
                            q.append((nr, nc))
        bfs(qp, vp)
        bfs(qa, va)

        ans = []
        for cell in va:
            if cell in vp:
                ans.append([cell[0], cell[1]])
        return ans