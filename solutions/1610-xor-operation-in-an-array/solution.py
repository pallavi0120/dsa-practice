class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xorr=0
        for i in range(n):
            xorr^=(start+(2*i))
        return xorr
