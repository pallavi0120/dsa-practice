class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c1=c2=c3=0
        op=[]
        for i in range(len(nums)):
            if nums[i]>0:
                c1+=1
            elif nums[i]<0:
                c2+=1
            else:
                c3+=1
        op.extend([c1,c2])
        return max(op)
