class Solution:
    def rotate(self, arr: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #Optimal Approach
        row = len(arr)
        col = len(arr[0])
        for i in range(row):
            for j in range(i): #10 01 20 02 21 12
                temp = arr[i][j]
                arr[i][j] = arr[j][i]
                arr[j][i] = temp
        for i in range(len(arr)):
            arr[i] = arr[i][::-1]



        #Brute Force

        # n = len(matrix)
        # rotated = [[ 0 for x in range(n)]for x in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         rotated[j][n-i-1] = matrix[i][j]
        
        # for i in range(n):
        #     for j in range(n):
        #         matrix[i][j] = rotated[i][j]        