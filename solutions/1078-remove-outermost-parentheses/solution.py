class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cl=0
        cr=0
        op=[]
        sl=[]
        l=list(s)
        for i in range(len(l)):
            if l[i]=='(':
                cl+=1
            else:
                cr+=1
            sl.append(l[i])
            if cl==cr:
                op.append(sl)
                sl=[]
        for i in range(len(op)):
            op[i].pop()
            op[i].pop(0)
        res=''
        for i in range(len(op)):
            for j in range(len(op[i])):
                res+=str(op[i][j])
        return res
