class Solution:
    def largestSqInHist(self,arr):
        st=[]
        n=len(arr)
        maxArea=0
        for i in range(n):
            while st and arr[st[-1]]>arr[i]:
                el=st[-1]
                st.pop()
                nse=i
                if st:
                    pse=st[-1]
                else:
                    pse=-1
                maxArea=max(maxArea,min((nse-pse-1),arr[el])**2)
            st.append(i)
        while st:
            el=st[-1]
            st.pop()
            nse=n
            if st:
                pse=st[-1]
            else:
                pse=-1
            maxArea=max(maxArea,min((nse-pse-1),arr[el])**2)
        return maxArea
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        height=[0]*m
        maxArea=0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=='1':
                    height[j]+=1
                else:
                    height[j]=0
            area=self.largestSqInHist(height)
            maxArea=max(maxArea,area)
        return maxArea
