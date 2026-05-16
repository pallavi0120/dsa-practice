class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n=len(weights)
        def func(arr,days,capacity):
            n=len(arr)
            day=1
            load=0
            for i in range(n):
                if load+arr[i]<=capacity:
                    load+=arr[i]
                else:
                    day+=1
                    load=arr[i]
            if day<=days:
                return True
            return False
        low=max(weights)
        high=sum(weights)
        while low<=high:
            mid=(low+high)//2
            if func(weights,days,mid)==True:
                high=mid-1
            else:
                low=mid+1
        return low   
            
