class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        for i in range(x+1):
            if x==(i)**2:
                return i
            if x<(i)**2:
                return i-1
            
        
