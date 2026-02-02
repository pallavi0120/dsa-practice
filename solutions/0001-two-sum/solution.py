class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic=dict()
        op=[]
        for i in range(len(nums)):
            if target-nums[i] not in dic.keys():
                dic[nums[i]]=i
            else:
                j=dic[target-nums[i]]
                op.append(j)
                op.append(i)
        return op
