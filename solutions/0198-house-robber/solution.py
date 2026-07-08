class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n+1)
        prev=nums[0]
        prev2=0
        for i in range(1,n):
            t=nums[i]
            if i>1:
                t+=prev2
            nt=prev
            curri=max(t,nt)
            prev2=prev
            prev=curri
        return prev
