# 既然是按顺时针填充，那就按照上、右、下、左的方法填写，由外向内
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[1]]
        matrix = [[0] * n for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        cur = 1
        while top < bottom and left < right:
            for j in range(left, right + 1):
                matrix[top][j] = cur
                cur += 1
            for i in range(top + 1, bottom):
                matrix[i][right] = cur
                cur += 1
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = cur
                cur += 1
            for i in range(bottom - 1, top, -1):
                matrix[i][left] = cur
                cur += 1
            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
        if top == bottom:
            for j in range(left, right + 1):
                matrix[top][j] = cur
                cur += 1
        elif left == right:
            for j in range(top, bottom + 1):
                matrix[i][right] = cur
                cur += 1
        return matrix

# 第二种方法，和螺旋矩阵I里的方法一样
# 就是一行一行添加，在添加的过程中改变矩阵的方向


def generateMatrix(self, n):
    matrix, lo = [], n * n + 1
    while lo > 1:
        lo, hi = lo - len(matrix), lo
        matrix = [range(lo, hi)] + zip(*matrix[::-1])
    return matrix
