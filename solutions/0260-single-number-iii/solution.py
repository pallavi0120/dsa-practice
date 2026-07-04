class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        n=len(nums)
        for i in range(n):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        op=[]
        for i in d.keys():
            if d[i]==1:
                op.append(i)
        return op
