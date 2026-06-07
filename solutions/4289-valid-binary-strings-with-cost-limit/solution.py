class Solution:
    def cost(self,stri):
        n=len(stri)
        sum=0
        for i in range(1,n):
            if stri[i]=='1':
                sum+=i
        return sum
    def notwoones(self,stri):
        c=0
        for i in range(len(stri)):
            if stri[i]=='1':
                c+=1
            else:
                c=0
            if c==2:
                return False
        return True
    def generatestr(self,n):
        op=[]
        for i in range(2**n):
            o=str(bin(i)[2:])
            if len(o)==n:
                op.append(o)
            else:
                o1='0'*(n-len(o))
                op.append(o1+o)
        return op
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        strs=self.generatestr(n)
        res=[]
        for i in range(len(strs)):
            if self.cost(strs[i])<=k and self.notwoones(strs[i]) is True:
                res.append(strs[i])
        return res
