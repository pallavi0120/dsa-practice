class Solution:
    def largestOddNumber(self, num: str) -> str:
        ind=-1
        n=len(num)
        for i in range(n-1,-1,-1):
            if int(num[i])%2==1:
                ind=i
                break
        i=0
        while i<ind and num[i]=='0':
            i+=1
        return num[i:ind+1]
