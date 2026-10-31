class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []
        # print(matrix)
        m = len(matrix)
        n = len(matrix[0])

        if m==0 or n==0:
            return []

        if m==1:
            return matrix[0]

        if n==1:
            res = []
            for item in matrix:
                res.append(item[0])
            return res

        i = 0
        j = 0

        res = []

        for i in range(0, n):
            res.append(matrix[0][i])

        # print(matrix, m, n)

        for i in range(1, m):
            res.append(matrix[i][n-1])

        for i in range(n-2, -1, -1):
            res.append(matrix[m-1][i])

        # print(res)
        

        for i in range(m-2, 0, -1):
            res.append(matrix[i][0])

        # print(res)

        remainder = []

        for row in matrix[1:-1]:
            remainder.append(row[1:-1])

        
        # if len(remainder) == len(matrix) or len(remainder[0]) == len(matrix[0]):
        #     return []

        return res + self.spiralOrder(remainder)
