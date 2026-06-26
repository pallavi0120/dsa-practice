class Solution:
    def nse(self,arr):
        st=[]
        n=len(arr)
        nse=[0]*n
        for i in range(n-1,-1,-1):
            while st and arr[i]<=arr[st[-1]]:
                st.pop()
            if st:
                nse[i]=st[-1]
            else:
                nse[i]=n
            st.append(i)
        return nse
    def psee(self,arr):
        n=len(arr)
        st=[]
        psee=[0]*n
        for i in range(n):
            while st and arr[i]<arr[st[-1]]:
                st.pop()
            if st:
                psee[i]=st[-1]
            else:
                psee[i]=-1
            st.append(i)
        return psee
    def sumSubarrayMins(self, arr: List[int]) -> int:
        total=0
        mod=(10**9)+7
        nse=self.nse(arr)
        psee=self.psee(arr)
        for i in range(len(arr)):
            left=i-psee[i]
            right=nse[i]-i
            total=(total+(left*right*arr[i])%mod)%mod
        return total
