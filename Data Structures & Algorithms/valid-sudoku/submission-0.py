class Solution(object):
    def isValidSudoku(self, board):
        rows = {}
        cols = {}
        sq = {}

        for i in range(9):
            rows[i] = set()
            cols[i] = set()
        for i in range(3):
            for j in range(3):
                sq[(i, j)] = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                val = board[i][j]
                if val in rows[i] or val in cols[j] or val in sq[(i // 3, j // 3)]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                sq[(i // 3, j // 3)].add(val)

        return True