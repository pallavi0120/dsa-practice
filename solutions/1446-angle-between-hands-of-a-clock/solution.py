class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour==12:
            hour=0
        h=(hour*5)+((5/60)*(minutes))
        m=minutes
        a=abs(h-m)
        return 6*min(a,60-a)
