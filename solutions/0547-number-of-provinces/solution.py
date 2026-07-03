from collections import deque
class Solution:
    def dfs(self,st,adjL,vis):
        vis[st]=True
        for i in adjL[st]:
            if not vis[i]:
                self.dfs(i,adjL,vis)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        adjL=[]
        for i in range(n):
            adjL.append([])
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    adjL[i].append(j)
                    adjL[j].append(i)
        vis=[False]*n
        c=0
        for i in range(n):
            if not vis[i]:
                c+=1
                self.dfs(i,adjL,vis)
        return c
