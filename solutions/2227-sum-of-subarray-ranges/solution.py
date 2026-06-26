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
    def pgee(self,arr):
        st=[]
        n=len(arr)
        pge=[0]*n
        for i in range(n):
            while st and arr[i]>arr[st[-1]]:
                st.pop()
            if st:
                pge[i]=st[-1]
            else:
                pge[i]=-1
            st.append(i)
        return pge
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
    def subArrayRanges(self, nums: List[int]) -> int:
        total1,total2=0,0
        nse=self.nse(nums)
        psee=self.psee(nums)
        nge=self.nge(nums)
        pgee=self.pgee(nums)
        for i in range(len(nums)):
            left1=i-psee[i]
            right1=nse[i]-i
            total1+=(left1*right1*nums[i])
            left2=i-pgee[i]
            right2=nge[i]-i
            total2+=(left2*right2*nums[i])
        return total2-total1
