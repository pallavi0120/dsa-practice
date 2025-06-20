class Solution:
    def maxDepth(self, s: str) -> int:
        cl=0
        cr=0
        l=[]
        for i in range(len(s)):
            if s[i]=='(':
                cl+=1
            if s[i]==')':
                cr+=1
            l.append(cl-cr)
        return max(l)
