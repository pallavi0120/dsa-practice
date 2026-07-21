class Solution:
    def findmax(self,grid,i,j):
        maxi=0
        x,y=i-1,j-1
        for x in range(i-1,i+2):
            for y in range(j-1,j+2):
                if grid[x][y]>maxi:
                    maxi=grid[x][y]
        return maxi
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        mat=[[0 for i in range(n-2)] for i in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                mat[i][j]=self.findmax(grid,i+1,j+1)
        return mat
