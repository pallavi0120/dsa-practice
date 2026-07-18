class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        l=list(s)
        n=len(l)
        if x not in l or y not in l:
            return s
        minx,maxy,cnt_x,cnt_y=-1,-1,0,0
        for i in range(n):
            if l[i]==x:
                minx=i
                break
        for i in range(n):
            if l[i]==y:
                maxy=i
                cnt_y+=1
            if l[i]==x:
                cnt_x+=1
        if maxy<minx:
            return s
        else:
            res=''
            res+=(y*(cnt_y))
            res+=(x*(cnt_x))
            for i in l:
                if i!=x and i!=y:
                    res+=i
            return res
