class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        h1,h2=int(startTime[0:2]),int(endTime[0:2])
        m1,m2=int(startTime[3:5]),int(endTime[3:5])
        s1,s2=int(startTime[6:8]),int(endTime[6:8])
        if s2==0 and s1!=0:
            s2=60
            m1+=1
        s=s2-s1
        if m1==60:
            h1+=1
            m1=0
        if m2==0 and m1!=0:
            m2=60
            h1+=1
        m=m2-m1
        if h2==0 and h1!=0:
            h2=24
        h=h2-h1
            
        return (h*(3600))+(m*(60))+s
