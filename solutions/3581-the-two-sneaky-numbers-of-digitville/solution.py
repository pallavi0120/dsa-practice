class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s=list(set(nums))
        op=[]
        for i in range(len(s)):
            if nums.count(s[i])==2:
                op.append(s[i])
        return op
