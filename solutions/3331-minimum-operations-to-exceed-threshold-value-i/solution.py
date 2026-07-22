class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt=0
        while min(nums)<k:
            nums.remove(min(nums))
            cnt+=1
        return cnt
