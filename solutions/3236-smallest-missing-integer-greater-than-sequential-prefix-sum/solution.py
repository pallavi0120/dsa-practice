class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]+1
        c,summ=1,nums[0]
        for i in range(1,n):
            if nums[i]==nums[i-1]+1:
                c+=1
                summ+=nums[i]
            else:
                break
        while summ in nums:
            summ+=1
        return summ
