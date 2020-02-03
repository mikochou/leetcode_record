# 二分查找, O(m+n)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix:
            r, c, w = len(matrix) - 1, 0, len(matrix[0])
            while r >= 0 and c < w:
                if matrix[r][c] == target:
                    return True
                elif matrix[r][c] > target:
                    r = r - 1
                else:
                    c = c + 1
        return False
