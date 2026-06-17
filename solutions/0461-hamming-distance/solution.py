class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        start,goal=x,y
        diff=len(bin(start))-len(bin(goal))
        if diff>0:
            bg=(diff*'0')+bin(goal)[2:]
            bs=bin(start)[2:]
        elif diff<0:
            bs=((-diff)*'0')+bin(start)[2:]
            bg=bin(goal)[2:]
        else:
            bs=bin(start)[2:]
            bg=bin(goal)[2:]
        xorr=''
        for i in range(len(bs)):
            xorr+=str(int(bs[i])^(int(bg[i])))
        return list(xorr).count('1')
