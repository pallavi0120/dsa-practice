import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        def func(arr,hourly):
            n=len(arr)
            totalhours=0
            for i in range(n):
                totalhours+=math.ceil(arr[i]/hourly)
            return totalhours
        low=1
        high=max(piles)
        while low<=high:
            mid=(low+high)//2
            if func(piles,mid)<=h:
                high=mid-1
            else:
                low=mid+1
        return low
