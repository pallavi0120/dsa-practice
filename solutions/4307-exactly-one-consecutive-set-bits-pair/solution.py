class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        b=int(bin(n)[2:])
        sb=str(b)
        c=0
        c1=0
        for i in range(len(sb)):
            if sb[i]=='1':
                c+=1
            else:
                if c>=2:
                    c1+=(c-1)
                c=0
        if c>0:
            c1+=(c-1)
        if c1==1:
            return True
        return False
