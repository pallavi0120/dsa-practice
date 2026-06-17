class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxInd=0
        for i in range(len(nums)):
            if i>maxInd:
                return False
            maxInd=max(maxInd,i+nums[i])
        return True
























        '''n=len(nums)
        if n==1:
            return True
        start=nums[1]
        i=0
        while i<n-1:
            if nums[i]==0:
                return False
            i+=nums[i]
        if i>=n-1:
            return True
        return False'''
