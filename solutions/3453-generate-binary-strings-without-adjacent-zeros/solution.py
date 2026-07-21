class Solution:
    def validStrings(self, n: int) -> List[str]:
        res=[]
        for i in range(2**n):
            b=str(bin(i)[2:])
            if len(b)!=n:
                b=('0'*(n-len(b)))+b
            if '00' not in b:
                res.append(b)
        return res
