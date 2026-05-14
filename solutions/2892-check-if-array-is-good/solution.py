class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=len(nums)
        nums.sort()
        c=0
        for i in range(n-1):
            if nums[i]==i+1:
                c+=1
        if c==n-1 and nums[n-1]==n-1:
            return True
        return False
