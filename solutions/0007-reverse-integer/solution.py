class Solution:
    def reverse(self, x: int) -> int:
        op=0
        a=abs(x)
        for i in range(len(str(a))):
            op+=int(str(a)[i])*(10**(i))
        if op<=2147483647 and op>=-2147483648:
            if x>=0:
                return op
            else:
                return -op
        else:
            return 0
