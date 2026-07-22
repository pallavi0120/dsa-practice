class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        cnt=0
        for i in nums:
            s=list(str(i))
            cnt+=s.count(str(digit))
        return cnt
