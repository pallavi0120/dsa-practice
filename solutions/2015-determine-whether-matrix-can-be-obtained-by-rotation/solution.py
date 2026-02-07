class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        def reverse(arr,start,end):
            if start>=end:
                return
            arr[start],arr[end]=arr[end],arr[start]
            reverse(arr,start+1,end-1)
        for i in range(4):
            for i in range(n-1):
                for j in range(i+1,n):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            for i in range(n):
                reverse(mat[i],0,n-1)
            if mat==target:
                return True
        return False
