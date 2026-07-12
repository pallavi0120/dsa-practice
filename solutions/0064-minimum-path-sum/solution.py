class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        int_max=10**9
        dp=[-1 for _ in range(n)]
        for i in range(m):
            temp=[-1 for _ in range(n)]
            for j in range(n):
                if i==0 and j==0:
                    temp[j]=grid[i][j]
                else:
                    up,left=grid[i][j],grid[i][j]
                    if i>0:
                        up+=dp[j]
                    else:
                        up+=int_max
                    if j>0:
                        left+=temp[j-1]
                    else:
                        left+=int_max
                    temp[j]=min(up,left)
            dp=temp
        return dp[n-1]
