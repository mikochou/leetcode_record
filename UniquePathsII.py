
# 同样使用动态规划的思想，增加判断和边界条件


def uniquePathsWithObstacles(self, A):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    m, n = len(A), len(A[0])
    dp = [[0] * n for _ in range(m)]
    if A[0][0] == 0:
        dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if A[i][j] == 0:
                if i == j == 0:
                    continue
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp)
    return dp[m - 1][n - 1]
