class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1]*(n+1)
        prev2,prev=0,0
        for ind in range(1,n+1):
            left=prev+cost[ind-1]
            right=0
            if ind>1:
                right=prev2+cost[ind-2]
            curri=min(left,right)
            prev2=prev
            prev=curri
        return prev
