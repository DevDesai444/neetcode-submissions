class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxa = 0
        dirc = [(1,0),(0,1),(-1,0),(0,-1)]
        vis = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in vis:
                    vis.add((i,j))
                    area = 0
                    if grid[i][j]==1:
                        q = [(i,j)]
                        area += 1
                        while q:
                            r,c = q.pop(0)
                            for d in range(len(dirc)):
                                (dr, dc) = dirc[d]
                                nr, nc = r + dr , c + dc
                                if (nr,nc) not in vis:
                                    vis.add((nr,nc))
                                    if (0<=nr<len(grid)) and (0<=nc<len(grid[0])) and (grid[nr][nc]==1) :
                                        area +=1
                                        q.append((nr,nc))
                    if area>=maxa:
                        maxa = area
        return maxa


                                    