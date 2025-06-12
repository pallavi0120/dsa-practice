class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        d={}
        s=list(set(nums))
        for i in s:
            d[nums.count(i)]=i
        c=max(d.keys())
        if c>(n//2):
            return d[c]
       
        
