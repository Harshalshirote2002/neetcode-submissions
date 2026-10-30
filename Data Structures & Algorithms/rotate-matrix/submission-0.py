class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        swapped = []
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in swapped:
                    matrix[i][j], matrix[j][m-i-1] = matrix[j][m-i-1], matrix[i][j]
                    swapped.append((i, j))
                    swapped.append((j, m-i-1))
                    # print(i, j)
                