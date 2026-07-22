class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            mini,ind=nums[0],0
            for j in range(1,len(nums)):
                if nums[j]<mini:
                    mini=nums[j]
                    ind=j
            nums[ind]*=multiplier
        return nums
            
