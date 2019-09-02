# 动态规划，A[i][j] = A[i-1][j]+A[i][j-1]
def uniquePaths(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    A = [[0] * m for j in range(n)]
    for i in range(n):
        for j in range(m):
            if i == j == 0:
                A[i][j] = 1
                continue
            A[i][j] = A[i - 1][j] + A[i][j - 1]
    return A[n - 1][m - 1]

# 上面的2d矩阵很慢，可以优化为一维


def uniquePaths(self, m, n):
    if not m or not n:
        return 0
    A = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            A[j] += A[j - 1]
    return A[-1]
