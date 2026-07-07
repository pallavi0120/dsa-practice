class Solution:
    def tribonacci(self, n: int) -> int:
        if n<3:
            if n<2:
                return n
            return 1
        prev0,prev1,prev2=0,1,1
        for i in range(3,n+1):
            curri=prev0+prev1+prev2
            prev0,prev1,prev2=prev1,prev2,curri
        return prev2
