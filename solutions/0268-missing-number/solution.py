class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        while i<len(nums):
            if i!=nums[i]:
                return i
                break
            else:
                i+=1
        if i==len(nums):
            return i
