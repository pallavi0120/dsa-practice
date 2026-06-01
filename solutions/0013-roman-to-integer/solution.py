'''class Solution:
    def romanToInt(self, s: str) -> int:
        D={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        output=0
        s=list(s)
        i=0
        while i<len(s)-1:
        #for i in range(len(s)-1):
            if D[s[i]]>=D[s[i+1]]:
                output+=D[s[i]]
                i+=1
            else:
                output+=(D[s[i+1]]-D[s[i]])
                i+=2
        if i==len(s)-1:
            output+=D[s[i]]
        #if i>len(s)-1:
            #break
        return output'''
class Solution:
    def romanToInt(self, s: str) -> int:
        D={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res=0
        for i in range(len(s)-1):
            if D[s[i]]<D[s[i+1]]:
                res-=D[s[i]]
            else:
                res+=D[s[i]]
        res+=D[s[-1]]
        return res
