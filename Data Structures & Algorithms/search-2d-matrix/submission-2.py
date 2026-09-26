class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n=len(matrix[0])

        start = 0
        end = m

        mid = 0

        while start<=end and mid<m:
            mid = int((start+end)/2)
            if mid >=m:
                mid-=1
                break
            rowStart = matrix[mid][0]
            rowEnd = matrix[mid][-1]

            if target >= rowStart and target <= rowEnd:
                break
            elif target < rowStart:
                end = mid - 1
            elif target > rowEnd:
                start = mid + 1

        if target in matrix[mid]:
            return True

        return False
