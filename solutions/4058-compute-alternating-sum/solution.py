class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        i=0
        op=0
        while i<len(nums):
            if i%2==0:
                op+=nums[i]
            else:
                op-=nums[i]
            i+=1
        return op
