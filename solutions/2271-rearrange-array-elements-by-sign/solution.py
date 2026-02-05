class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=0
        neg=1
        n=len(nums)
        ans=[0]*n
        i=0
        while i<n:
            if nums[i]<0:
                ans[neg]=nums[i]
                neg+=2
                i+=1
            else:
                ans[pos]=nums[i]
                pos+=2
                i+=1
        return ans
