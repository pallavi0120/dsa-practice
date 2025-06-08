class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num>0 and num<2147483648:
            for i in range(num+1):
                if num==(i)**2:
                    return True
                if num<(i)**2:
                    return False

