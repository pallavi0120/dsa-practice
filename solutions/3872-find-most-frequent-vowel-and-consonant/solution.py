class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels=['a','e','i','o','u']
        cntv,cntc=0,0
        sett=set(s)
        listt=list(s)
        for i in sett:
            if i in vowels:
                if listt.count(i)>cntv:
                    cntv=listt.count(i)
            else:
                if listt.count(i)>cntc:
                    cntc=listt.count(i)
        return cntv+cntc
