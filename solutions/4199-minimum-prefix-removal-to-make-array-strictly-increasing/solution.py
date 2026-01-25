class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        for i in range(n-1):
            if nums[n-i-1]>nums[n-i-2]:
                c+=1
            else: 
                l=n-i-1
                return l
        if c==n-1:
            return 0
