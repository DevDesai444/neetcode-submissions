class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(i,j):
            if (i,j) not in visited:
                visited.add((i,j))
                for dr, dc in directions :
                    nr, nc = i+dr, j+ dc
                    if (0<=nr<len(board)) and (0<=nc<len(board[0])) and ((nr,nc) not in visited) and (board[nr][nc]=='O'):
                        # visited.add((nr,nc))
                        dfs(nr,nc)
        
        for i in range(len(board)):
            if (board[i][0]=='O') and ((i,0) not in visited):
                dfs(i,0)
            if (board[i][len(board[0])-1]=='O') and ((i,len(board[0])-1) not in visited):
                dfs(i,len(board[0])-1)
        
        for i in range(len(board[0])):
            if (board[0][i]=='O') and ((0,i) not in visited):
                dfs(0,i)
            if (board[len(board)-1][i]=='O') and ((len(board)-1, i) not in visited):
                dfs(len(board)-1, i)
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                if ((i,j) not in visited) and (board[i][j]=='O') :
                    board[i][j]='X'