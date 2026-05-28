class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n=len(s)
        c=0
        res=''
        for i in range(n):
            if s[i]=='(':
                c+=1
                if c>1:
                    res+='('
            else:
                c-=1
                if c>0:
                    res+=')'
        return res
