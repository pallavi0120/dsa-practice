class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            if matrix[i][0]<=target<=matrix[i][m-1]:
                if target in matrix[i]:
                    return True
        return False
