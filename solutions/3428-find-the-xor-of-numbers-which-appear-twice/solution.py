class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ans=0
        seen=0
        for x in nums:
            if seen&(1<<x):
                ans^=x
            else:
                seen|=(1<<x)
        return ans
