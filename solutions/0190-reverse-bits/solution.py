class Solution:
    def reverseBits(self, n: int) -> int:
        r=bin(n)[2:]
        r=r[::-1]
        if len(r)!=32:
            r+='0'*(32-len(r))
        n=len(r)
        p2=1
        num=0
        for i in range(n-1,-1,-1):
            if r[i]=='1':
                num+=p2
            p2*=2
        return num
