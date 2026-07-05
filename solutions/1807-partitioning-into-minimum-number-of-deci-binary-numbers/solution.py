class Solution:
    def minPartitions(self, n: str) -> int:
        maxx=0
        for i in n:
            i=int(i)
            if i>maxx:
                maxx=i
        return maxx
