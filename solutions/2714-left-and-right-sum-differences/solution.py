class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        op=[]
        l=[0]
        r=[0]
        for i in range(len(nums)-1):
            l.append(nums[i]+l[i])
            r.append(nums[len(nums)-1-i]+r[i])
        r=r[::-1]
        for i in range(len(nums)):
            op.append(abs(l[i]-r[i]))
        return op
