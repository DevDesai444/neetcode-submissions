class Solution:
    def numIslands(self, grid):
        visited = set()
        count = 0
        dirct = [(0,1),(1,0),(-1,0),(0,-1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    count += 1
                    q = [(i,j)]
                    visited.add((i,j))
                    while q:
                        r, c = q.pop(0)
                        for d in range(len(dirct)):
                            di, dj = dirct[d]
                            nr, nc = r + di, c + dj
                            if (nr, nc) not in visited :
                                visited.add((nr, nc))
                                if (0 <= nr < len(grid)) and (0 <= nc < len(grid[0])) and grid[nr][nc] == "1":
                                    q.append((nr, nc))
        return count