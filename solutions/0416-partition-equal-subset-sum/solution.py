class Solution:
    def f(self,ind,k,arr):
        n=len(arr)
        dp=[0 for i in range(k+1)] 
        dp[0]=True
        if arr[0]<=k:
            dp[arr[0]]=True
        for ind in range(1,n):
            curr=[0 for i in range(k+1)]
            curr[0]=True
            for target in range(1,k+1):
                nottake=dp[target]
                take=False
                if arr[ind]<=target:
                    take=dp[target-arr[ind]]
                curr[target]=take or nottake
            dp=curr
        if dp[k]==True or False:
            return dp[k]
        elif dp[k]==0:
            return False
        else:
            return True
    def canPartition(self, nums: List[int]) -> bool:
        summ=sum(nums)
        if summ%2!=0:
            return False
        else:
            target=summ//2
            return self.f(0,target,nums)
