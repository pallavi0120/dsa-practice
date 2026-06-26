class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        st=[]
        n=len(heights)
        for i in range(n):
            while st and heights[st[-1]]>heights[i]:
                element=st[-1]
                st.pop()
                nse=i
                if st:
                    pse=st[-1]
                else:
                    pse=-1
                maxArea=max(maxArea,(nse-pse-1)*heights[element])
            st.append(i)
        while st:
            nse=n
            el=st[-1]
            st.pop()
            if st:
                pse=st[-1]
            else:
                pse=-1
            maxArea=max(maxArea,(nse-pse-1)*heights[el])
        return maxArea
