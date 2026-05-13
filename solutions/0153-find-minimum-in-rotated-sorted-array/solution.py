class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=n-1
        ans=5001
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=nums[high]:
                ans=min(ans,nums[low])
                break
            if nums[low]<=nums[mid]:
                ans=min(ans,nums[low])
                low=mid+1
            else:
                ans=min(nums[mid],ans)
                high=mid-1
        return ans
