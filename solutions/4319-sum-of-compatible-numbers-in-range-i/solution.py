class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        sum=0
        #mini=min(abs(n-k),n,k)
        for x in range(1,n+k+1):
            if abs(n-x)<=k and (n&x)==0:
                sum+=x
        return sum
