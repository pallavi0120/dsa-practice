class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #if n!=1:
            if n==0 or n<0:
                return False
            for i in range(n):
                if n==2**(i):
                    return True
                if n<2**(i):
                    return False
