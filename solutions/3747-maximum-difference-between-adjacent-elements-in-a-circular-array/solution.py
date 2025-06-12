class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        d=[]
        for i in range(len(nums)-1):
            d.append(abs(nums[i]-nums[i+1]))
        d.append(abs(nums[0]-nums[len(nums)-1]))
        return max(d)
        
