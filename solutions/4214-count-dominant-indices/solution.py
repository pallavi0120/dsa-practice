class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        for i in range(0,n-1):
            sum=0
            c1=0
            for j in range(i+1,n):
                sum+=nums[j]
                c1+=1
            avg=sum/c1
            if nums[i]>avg:
                c+=1
        return c
