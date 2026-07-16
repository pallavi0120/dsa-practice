class Solution:
    def f(self,i,j1,j2,m,n,a,dp):
        if j1<0 or j2<0 or j1>=m or j2>=m:
            return -1e8
        if dp[i][j1][j2]!=-1:
            return dp[i][j1][j2]
        if i==n-1:
            if j1==j2:
                return a[i][j1]
            else:
                return a[i][j1]+a[i][j2]
        maxi=0
        for dj1 in range(-1,2):
            for dj2 in range(-1,2):
                if j1==j2:
                    maxi=max(maxi,a[i][j1]+self.f(i+1,j1+dj1,j2+dj2,m,n,a,dp))
                else:
                    maxi=max(maxi,a[i][j1]+a[i][j2]+self.f(i+1,j1+dj1,j2+dj2,m,n,a,dp))
        dp[i][j1][j2]=maxi
        return dp[i][j1][j2]
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[-1 for i in range(m)] for i in range(m)]
        curr=[[-1 for i in range(m)] for i in range(m)]
        for j1 in range(0,m):
            for j2 in range(0,m):
                if j1==j2:
                    dp[j1][j2]=grid[n-1][j2]
                else:
                    dp[j1][j2]=grid[n-1][j1]+grid[n-1][j2]
        for i in range(n-2,-1,-1):
            for j1 in range(0,m):
                for j2 in range(0,m):
                    maxi=-1e8
                    value=0
                    if j1==j2:
                        value=grid[i][j1]
                    else:
                        value=grid[i][j1]+grid[i][j2]
                    for dj1 in range(-1,2):
                        for dj2 in range(-1,2):
                            if 0<=j1+dj1<m and 0<=j2+dj2<m:
                                maxi=max(maxi,value+dp[j1+dj1][j2+dj2])
                            else:
                                maxi=max(maxi,-1e8)
                    curr[j1][j2]=maxi
            dp=[row[:] for row in curr]
        return dp[0][m-1]
        
