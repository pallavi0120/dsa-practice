class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        ind=-1
        def reverse(arr,start,end):
            if start>=end:
                return
            arr[start],arr[end]=arr[end],arr[start]
            reverse(arr,start+1,end-1)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind=i
                break
        if ind==-1:
            reverse(nums,0,n-1)
        else:
            for i in range(n-1,ind,-1):
                if nums[i]>nums[ind]:
                    nums[i],nums[ind]=nums[ind],nums[i]
                    break
            reverse(nums,ind+1,n-1)
