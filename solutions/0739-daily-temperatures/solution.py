class Solution:
    def nge(self,arr):
        st=[]
        n=len(arr)
        nge=[0]*n
        for i in range(n-1,-1,-1):
            while st and arr[i]>=arr[st[-1]]:
                st.pop()
            if st:
                nge[i]=st[-1]
            else:
                nge[i]=n
            st.append(i)
        return nge
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nge=self.nge(temperatures)
        n=len(temperatures)
        op=[0]*n
        for i in range(len(temperatures)):
            if nge[i]!=n:
                op[i]=nge[i]-i
            else:
                op[i]=0
        return op
