class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        d=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    d.append(nums[j]-nums[i])
        if d==[]:
            return -1
        else:
            return max(d)

        
