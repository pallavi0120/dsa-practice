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
            op=[]
            for i in range(n):
                resi=''
                for j in range(n):
                    resi+=board[i][j]
                op.append(resi)
            res.append(op)
            return
        for row in range(n):
            if self.isSafe(row,col,board,n):
                board[row][col]="Q"
                self.f(col+1,board,res,n)
                board[row][col]="."
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[]
        for i in range(n):
            board.append(["."]*n)
        res=[]
        self.f(0,board,res,n)
        return res
