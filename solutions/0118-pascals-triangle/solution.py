class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n=numRows
        def generaterow(n):
            ans=1
            temp=[]
            temp.append(1)
            for i in range(1,n):
                ans=ans*(n-i)
                ans//=i
                temp.append(ans)
            return temp
        #def pascaltriangle(n):
        ans=[]
        for i in range(1,n+1):
            ans.append(generaterow(i))
        return ans


        
