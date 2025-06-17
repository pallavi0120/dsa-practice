class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)>1:
            l1=[]
            for i in range(len(nums)-1):
                l1.append((nums[i]+nums[i+1])%10)
            nums=l1
        return nums[0]
