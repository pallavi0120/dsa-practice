class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        op=nums
        for i in range(1,len(nums)):
            op[i]=op[i]+op[i-1]
        return op
