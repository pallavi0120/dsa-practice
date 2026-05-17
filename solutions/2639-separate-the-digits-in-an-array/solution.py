class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l=[]
        n=len(nums)
        for i in range(n):
            l+=list(str(nums[i]))
        l1=[]
        for i in range(len(l)):
            l1.append(int(l[i]))
        return l1
