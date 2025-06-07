class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0 or n<0:
            return False
        for i in range(n):
            if n==4**(i):
                return True
            if n<4**(i):
                return False

        
