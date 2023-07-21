class Solution:
    def col(self, i, matrix, m):
        for j in range(m):
            if matrix[i][j] != 0:
                matrix[i][j] = "a"

    def row(self, j, matrix, n):
        for i in range(n):
            if matrix[i][j] != 0:
                matrix[i][j] = "a"

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)         # number of rows [1st] [2nd] [3rd]
        m = len(matrix[0])      # number of columns 3

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    self.col(i, matrix, m)
                    self.row(j, matrix, n)

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "a":
                    matrix[i][j] = 0

   