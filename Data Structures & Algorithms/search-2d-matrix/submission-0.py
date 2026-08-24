class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n, m = len(matrix), len(matrix[0])
        low, high = 0, n * m - 1

        while low <= high:
            mid = (low + high) // 2
            val = matrix[mid // m][mid % m]
            if val < target:
                low = mid + 1
            elif val > target:
                high = mid - 1
            else:
                return True
        return False