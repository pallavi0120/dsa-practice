class Solution:
    def isSafe(self,row,col,board,n):
        duprow=row
        dupcol=col
        while row>=0 and col>=0:
            if board[row][col]=="Q":
                return False
            row-=1
            col-=1
        row=duprow
        col=dupcol
        while col>=0:
            if board[row][col]=="Q":
                return False
            col-=1
        row=duprow
        col=dupcol
        while row<n and col>=0:
            if board[row][col]=="Q":
                return False
            row+=1
            col-=1
        row=duprow
        col=dupcol
        return True
    def f(self,col,board,res,n):
        if col==n:
            res[0]+=1
            return
        for row in range(n):
            if self.isSafe(row,col,board,n):
                board[row][col]="Q"
                self.f(col+1,board,res,n)
                board[row][col]="."
    def totalNQueens(self, n: int) -> int:
        board=[]
        for i in range(n):
            board.append(["."]*n)
        res=[0]
        self.f(0,board,res,n)
        return res[0]
