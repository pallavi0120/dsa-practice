class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n=rowIndex+1
        ans=1
        temp=[]
        temp.append(1)
        for i in range(1,n):
            ans*=(n-i)
            ans//=i
            temp.append(ans)
        return temp
