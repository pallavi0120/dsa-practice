'''class Solution:
    def isTrue(self,board,l1,row,col,l2):
        if board[row][col]!=l1:
            return False
        n=len(board)
        m=len(board[0])
        duprow=row
        dupcol=col
        while row>=0:
            if board[row-1][col]==l2:
                return True
        #while row>=0 and col<m:
         #   if board[row-1][col+1]==l2:
          #      return True
        while col<m:
            if board[row][col+1]==l2:
                return True
        #while row<n and col<m:
         #   if board[row+1][col+1]==l2:
          #      return True
        while row <n:
            if board[row+1][col]==l2:
                return True
        #while row<n and col>=0:
         #   if board[row+1][col-1]==l2:
          #      return True
        while col>=0:
            if board[row][col-1]==l2:
                return True
        #while row>=0 and col>=0:
         #   if board[row-1][col-1]==l2:
          #      return True
        return False
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        w=list(word)
        for i in range(n):
            if w[0] in board[i]:
                row=i
                col=board[i].index(w[0])
        for i in range(1,len(word)):
            if self.isTrue(board,w[i-1],)'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        def dfs(i,j,idx):
            if idx==len(word):
                return True
            if i<0 or j<0 or i>=rows or j>=cols or board[i][j]!=word[idx]:
                return False
            temp=board[i][j]
            board[i][j]='#'
            found = dfs(i-1,j,idx+1) or dfs(i+1,j,idx+1) or dfs(i,j-1,idx+1) or dfs(i,j+1,idx+1)
            board[i][j]=temp
            return found
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False

