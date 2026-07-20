class Solution:
    def shift(self,grid):
        n=len(grid)
        m=len(grid[0])
        temp=grid[n-1][m-1]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if j!=0:
                    grid[i][j]=grid[i][j-1]
                else:
                    if i!=0:
                        grid[i][j]=grid[i-1][m-1]
                    else:
                        grid[i][j]=temp
        return grid
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n=len(grid)
        m=len(grid[0])
        n1=n*m
        k=k%n1
        for i in range(k):
            grid1=self.shift(grid)
            grid=grid1
        return grid
