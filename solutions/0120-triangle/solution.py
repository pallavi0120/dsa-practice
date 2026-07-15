class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[0 for i in range(n)] 
        for i in range(0,n):
            dp[i]=triangle[n-1][i]
        for i in range(n-2,-1,-1):
            temp=[0 for i in range(n)]
            for j in range(0,i+1):
                d=triangle[i][j]+dp[j]
                dg=triangle[i][j]+dp[j+1]
                temp[j]=min(d,dg)
            dp=temp
        return dp[0]
