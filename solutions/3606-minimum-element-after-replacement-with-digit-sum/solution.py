class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x=0
            for j in str(nums[i]):
                x+=int(j)
            nums[i]=x
        return min(nums)
