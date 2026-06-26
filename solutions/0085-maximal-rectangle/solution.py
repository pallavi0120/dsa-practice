class Solution:
    def largestRectInHist(self,arr):
        st,maxArea,n=[],0,len(arr)
        for i in range(n):
            while st and arr[st[-1]]>arr[i]:
                el=st[-1]
                st.pop()
                nse=i
                if st:
                    pse=st[-1]
                else:
                    pse=-1
                maxArea=max(maxArea,(nse-pse-1)*arr[el])
            st.append(i)
        while st:
            nse=n
            el=st[-1]
            st.pop()
            if st:
                pse=st[-1]
            else:
                pse=-1
            maxArea=max(maxArea,(nse-pse-1)*arr[el])
        return maxArea
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        heights=[0]*m
        maxArea=0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=='1':
                    heights[j]+=1
                else:
                    heights[j]=0
            area=self.largestRectInHist(heights)
            maxArea=max(maxArea,area)
        return maxArea
