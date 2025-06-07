class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def bintodec(n):
            op=0
            for i in range(len(str(n))):
                op+=int(str(n)[i])*(2**(len(str(n))-i-1))
            return op
        def dectobin(n):
            op=''
            while n!=1:
                op+=str(n%2)
                n=n//2
            op+=str(1)
            return op[::-1]
        if a=='0' and b=='0':
            return '0'
        else:
            return str(dectobin(bintodec(int(a))+bintodec(int(b))))
        
