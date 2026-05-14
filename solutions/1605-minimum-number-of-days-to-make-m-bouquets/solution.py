class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        def possible(arr,day,m,k):
            n=len(arr)
            count=0
            noofB=0
            for i in range(n):
                if arr[i]<=day:
                    count+=1
                else:
                    noofB+=(count//k)
                    count=0
            noofB+=(count//k)
            if noofB>=m:
                return True
            return False
        if n<(m*k):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        while low<=high:
            mid=(low+high)//2
            if possible(bloomDay,mid,m,k)==True:
                high=mid-1
            else:
                low=mid+1
        return low
        '''
    def possible(arr,day,m,k):
        n=len(arr)
        count=0
        noofB=0
        for i in range(n):
            if arr[i]<=day:
                count+=1
            else:
                noofB+=(count//3)
                count=0
        noofB+=(count//3)
        if noofB>=m:
            return True
        return False
        '''
