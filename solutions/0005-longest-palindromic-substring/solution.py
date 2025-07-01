class Solution:
    def longestPalindrome(self, s: str) -> str:
        l={}
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                st=s[i:j+1]
                if st==st[::-1]:
                    l[len(st)]=st
        if l.keys():
            m=max(l.keys())
            return l[m]
        return s[0]
        
