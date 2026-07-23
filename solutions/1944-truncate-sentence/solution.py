class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words=s.split(' ')
        res=''
        for i in range(k-1):
            res+=words[i]
            res+=' '
        res+=words[k-1]
        return res
