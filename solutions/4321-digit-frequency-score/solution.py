class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        op=0
        n=list(str(n))
        s=set(n)
        for i in s:
            op+=(int(i)*n.count(i))
        return op
