class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        '''sa=[] 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                sa.append(max(nums[i:j])-min(nums[i:j]))
        sa.sort()
        sa.reverse()
        return sa[0]*k'''
        return k*(max(nums)-min(nums))
