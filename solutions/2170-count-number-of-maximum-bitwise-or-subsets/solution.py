class Solution:
    def orr(self,arr):
        orr=0
        for i in arr:
            orr|=i
        return orr
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        orr=0
        for i in nums:
            orr|= i
        n=len(nums)
        subsets=1<<n
        c=0
        for num in range(subsets):
            xorr=0
            for i in range(n):
                if num&(1<<i):
                    xorr|=nums[i]
            if xorr==orr:
                c+=1
        return c
