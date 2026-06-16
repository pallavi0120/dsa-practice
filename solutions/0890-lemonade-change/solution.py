class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        noof5s=0
        noof10s=0
        for i in bills:
            if i==5:
                noof5s+=1
            elif i==10:
                if noof5s:
                    noof5s-=1
                    noof10s+=1
                else:
                    return False
            else:
                if noof5s>0 and noof10s>0:
                    noof5s-=1
                    noof10s-=1
                elif noof5s>2:
                    noof5s-=3
                else:
                    return False
        return True
