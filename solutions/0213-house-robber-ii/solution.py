class Solution:
    def f(self,arr):
        n=len(arr)
        prev=arr[0]
        prev2=0
        for i in range(1,n):
            t=arr[i]
            if i>1:
                t+=prev2
            nt=prev
            curri=max(t,nt)
            prev2=prev
            prev=curri
        return prev
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        nums1,nums2=[],[]
        for i in range(n):
            if i!=0:
                nums1.append(nums[i])
            if i!=n-1:
                nums2.append(nums[i])
        return max(self.f(nums1),self.f(nums2))
