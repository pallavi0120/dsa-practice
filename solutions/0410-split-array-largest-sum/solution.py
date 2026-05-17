class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        def func(arr,k,capacity):
            n=len(arr)
            load=0
            p=1
            for i in range(n):
                if load+arr[i]>capacity:
                    p+=1
                    load=arr[i]
                else:
                    load+=arr[i]
            if p>k:
                return False
            return True
        while low<=high:
            mid=(low+high)//2
            if func(nums,k,mid)==True:
                high=mid-1
            else:
                low=mid+1
        return low
