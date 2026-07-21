class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        one=abs(x-z)
        two=abs(y-z)
        if one<two:
            return 1
        elif two<one:
            return 2
        else:
            return 0
