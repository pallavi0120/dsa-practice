import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        def func(arr,threshold,div):
            n=len(arr)
            sum=0
            for i in range(n):
                sum+=math.ceil(arr[i]/div)
            return sum
        low=1
        high=max(nums)
        while low<=high:
            mid=(low+high)//2
            if func(nums,threshold,mid)<=threshold:
                high=mid-1
            else:
                low=mid+1
        return low
        if n>threshold:
            return -1
