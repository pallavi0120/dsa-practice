class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign=True
        if dividend<0 and divisor>0:
            sign=False
        if dividend>=0 and divisor<0:
            sign=False
        n,d=abs(dividend),abs(divisor)
        ans=0
        while n>=d:
            cnt=0
            while n>=(d<<(cnt+1)):
                cnt+=1
            ans+=(1<<cnt)
            n-=(d<<cnt)
        if ans>=2**31:
            if sign==True:
                return (2**31)-1
            return -(2**31)
        if sign==True:
            return ans
        return -1*ans
