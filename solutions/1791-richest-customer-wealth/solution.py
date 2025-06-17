class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        op=[]
        for i in range(len(accounts)):
            sum=0
            for j in range(len(accounts[i])):
                sum+=accounts[i][j]
            op.append(sum)
        return max(op)
