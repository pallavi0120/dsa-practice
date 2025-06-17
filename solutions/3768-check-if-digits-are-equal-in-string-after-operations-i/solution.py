class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            s1=''
            for i in range(len(s)-1):
                s1+=str((int(s[i])+int(s[i+1]))%10)
            s=s1
        return s[0]==s[1]
