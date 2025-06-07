class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0 or n<0:
            return False
        for i in range(n):
            if n==3**(i):
                return True
            if n<3**(i):
                return False
        
