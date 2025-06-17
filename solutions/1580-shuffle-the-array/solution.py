class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        op=[]
        for i in range(n):
            op.append(nums[i])
            op.append(nums[n+i])
        return op
