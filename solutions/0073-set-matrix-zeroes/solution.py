class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zero_positions = []

        # Step 1: Store the positions of all zeroes
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_positions.append((i, j))

        # Step 2: Zero the rows and columns for each zero position
        for i, j in zero_positions:
            self.func1(matrix, i)  # Set row to zero
            self.func2(matrix, j)  # Set column to zero

    def func1(self, matrix, row):
        for j in range(len(matrix[0])):
            matrix[row][j] = 0

    def func2(self, matrix, col):
        for i in range(len(matrix)):
            matrix[i][col] = 0

