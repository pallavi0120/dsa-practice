class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d1={}
        for ind,char in enumerate(s):
            d1[char]=ind
        summ=0
        for ind,char in enumerate(t):
            summ+=abs(ind-d1[char])
        return summ
