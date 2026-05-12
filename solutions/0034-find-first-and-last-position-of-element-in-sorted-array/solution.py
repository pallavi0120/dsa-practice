class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answ=[]
        n=len(nums)
        def lowerbound(nums,target):
            low=0
            high=n-1
            ans=n
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>=target:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            answ.append(ans)
            return ans
        def upperbound(nums,target):
            low=0
            high=n-1
            ans=n
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>target:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            answ.append(ans-1)
            return ans
        lb=lowerbound(nums,target)
        ub=upperbound(nums,target)

        if lb==n or nums[lb]!=target:
            return [-1,-1]
        return answ

