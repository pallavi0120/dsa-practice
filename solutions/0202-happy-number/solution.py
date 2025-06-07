class Solution:
    def isHappy(self, n: int) -> bool:
        l=[]
        while True:
            op=0
            for i in range(len(str(n))):
                op+=int(str(n)[i])**2
            n=op
            l.append(n)
            if n==1:
                return True
            if len(l)!=len(set(l)):
                return False
            if n>(2**(31)-1):
                return False


        
