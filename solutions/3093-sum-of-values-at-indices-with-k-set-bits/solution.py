class Solution:
    def noOfsetbits(self,n):
        c=0
        while n!=0:
            n=n&(n-1)
            c+=1
        return c
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        n=len(nums)
        summ=0
        for i in range(n):
            if self.noOfsetbits(i)==k:
                summ+=nums[i]
        return summ
