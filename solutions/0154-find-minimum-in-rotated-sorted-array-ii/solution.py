class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=n-1
        ans=5001
        while low<=high:
            mid=(low+high)//2
            if low==mid and mid==high:
                ans=min(ans,nums[mid])
            if low==mid and nums[low]==nums[high]:
                ans=min(ans,nums[low])
            if nums[low]==nums[mid] and nums[mid]==nums[high]:
                low+=1
                high-=1
                continue
            #if nums[low]<=nums[high]:
             #   ans=min(ans,nums[low])
              #  break
            if nums[low]<=nums[mid]:
                ans=min(ans,nums[low])
                low=mid+1
            if nums[mid]<=nums[high]:
                ans=min(ans,nums[mid])
                high=mid-1
            else:
                continue
        return ans
