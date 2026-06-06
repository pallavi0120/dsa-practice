class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c=0
        sumi=sum(nums)
        while sumi%k!=0:
            sumi-=1
            c+=1
        return c
