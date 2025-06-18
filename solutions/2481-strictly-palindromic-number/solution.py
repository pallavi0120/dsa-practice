class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        fn=n
        for i in range(2,fn-1):
            n=fn
            aftrconv=''
            while n>0:
                aftrconv+=str(n%i)
                n=n//i
            if aftrconv!=aftrconv[::-1]:
                return False
        return True
