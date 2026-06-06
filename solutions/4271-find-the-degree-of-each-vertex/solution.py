class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        op=[]
        for i in range(len(matrix)):
            op.append(sum(matrix[i]))
        return op
