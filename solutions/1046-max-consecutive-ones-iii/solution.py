class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        maxlen=0
        zeroes=0
        for right in range(len(nums)):
            if nums[right]==0:
                zeroes+=1
            
            #if zeroes>k, shrinking from left
            if zeroes>k:
                if nums[left]==0:
                    zeroes-=1
                left+=1

            #optional(then return maxlen)
            #maxlen=max(maxlen,right-left+1)
        return right-left+1
