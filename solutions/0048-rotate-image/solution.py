class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        def reverse(arr,start,end):
            if start>=end:
                return
            arr[start],arr[end]=arr[end],arr[start]
            reverse(arr,start+1,end-1)
        for i in range(n-1):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            reverse(matrix[i],0,n-1)
