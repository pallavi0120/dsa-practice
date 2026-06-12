class Solution:
    def isValid(self,ch,row,col,board):
        for i in range(9):
            if i!=row and board[i][col]==ch:
                return False
        for j in range(9):
            if j!=col and board[row][j]==ch:
                return False
        r=3*(row//3)
        c=3*(col//3)
        for i in range(3):
            for j in range(3):
                if ((r+i)!=row and (c+j)!=col) and board[r+i][c+j]==ch:
                    return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    if not self.isValid(board[i][j],i,j,board):
                        return False
        return True
