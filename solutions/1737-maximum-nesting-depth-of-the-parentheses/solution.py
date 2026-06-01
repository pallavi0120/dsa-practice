'''class Solution:
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
        return max(l)'''

class Solution:
    def maxDepth(self, s: str) -> int:
        ans=0
        counter=0
        for i in range(len(s)):
            if s[i]=='(':
                counter+=1
                #ans=max(ans,counter) or
            elif s[i]==')':
                counter-=1
            else:
                continue
            ans=max(ans,counter)
        return ans
