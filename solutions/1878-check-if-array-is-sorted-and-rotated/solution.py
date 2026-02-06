class Solution:
    def check(self, nums: List[int]) -> bool:
        def reverse(arr,start,end):
            if start>=end:
                return
            arr[start],arr[end]=arr[end],arr[start]
            reverse(arr,start+1,end-1)
        def rotate(nums,k):
            n=len(nums)
            reverse(nums,0,n-k-1)
            reverse(nums,n-k,n-1)
            reverse(nums,0,n-1)
        def sorted(arr):
            for i in range(len(arr)-1):
                if arr[i]>arr[i+1]:
                    return False
            return True
        for i in range(len(nums)):
            rotate(nums,1)
            if sorted(nums)==True:
                return True
        return False
