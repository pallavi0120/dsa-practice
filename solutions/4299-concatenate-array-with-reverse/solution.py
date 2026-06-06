class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        op=[]
        op+=nums
        nums.reverse()
        return op+nums
