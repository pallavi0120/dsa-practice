class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        n=len(num)
        for i in range(n):
            while st and k>0 and int(st[-1])>int(num[i]):
                st.pop()
                k-=1
            st.append(num[i])
        while st and k>0:
            st.pop()
            k-=1
        if not st:
            return '0'
        res,i='',0
        while st and st[0]=='0':
            st.pop(0)
        while st and i<len(st):
            res+=st[i]
            i+=1
        if not res:
            return '0'
        else:
            return res
