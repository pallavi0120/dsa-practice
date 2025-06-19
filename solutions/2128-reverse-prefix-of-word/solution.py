class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l=list(word)
        if ch in l:
            for i in range(len(l)):
                if l[i]==ch:
                    stoppingindex=i
                    break
            l0=l[:(stoppingindex+1)]
            l1=l0[::-1]
            l2=l[(stoppingindex+1):len(l)]
            fl=l1+l2
            res=''
            for i in fl:
                res+=i
            return res
        return word
