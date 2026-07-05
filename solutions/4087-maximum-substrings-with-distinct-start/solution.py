class Solution:
    def maxDistinct(self, s: str) -> int:
        seen=0
        c=0
        for i in s:
            if seen&(1<<(ord(i)-96))==0:
                c+=1
                seen|=(1<<(ord(i)-96))
        return c
