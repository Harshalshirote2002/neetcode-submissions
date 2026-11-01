class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i not in rows:
                        rows.append(i)
                    if j not in cols:
                        cols.append(j)

        # print(pairs)

        for row in rows:
            for k in range(0, len(matrix[0])):
                matrix[row][k] = 0
        for col in cols:
            for k in range(0, len(matrix)):
                matrix[k][col] = 0
            

            