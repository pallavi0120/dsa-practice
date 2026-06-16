class Solution:
    def processStr(self, s: str) -> str:
        res=''
        s=list(s)
        for i in range(len(s)):
            if s[i]=='*':
                if res:
                    res=res[:len(res)-1]
            elif s[i]=='#':
                res+=res
            elif s[i]=='%':
                res=res[::-1]
            else:
                res+=s[i]
        return res
