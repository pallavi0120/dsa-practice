class Solution:
    def divisorGame(self, n: int) -> bool:
        c=0
        while n>1: 
            x=1
            while x<n:
                if n%x==0:
                    c+=1
                    n=n-x

        if c%2!=0:
            return True
        else:
            return False
        
