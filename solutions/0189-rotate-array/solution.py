class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(arr,start,end):
            if start>=end:
                return
            arr[start],arr[end]=arr[end],arr[start]
            reverse(arr,start+1,end-1)
        n=len(nums)
        k=k%n
        reverse(nums,0,n-k-1)
        reverse(nums,n-k,n-1)
        reverse(nums,0,n-1)
        return nums
        
