# 动态规划，dp[i][j] = min(dp[i-1][j], dp[i][j-1])
def minPathSum(self, A):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m, n = len(A), len(A[0])
    if not m and n:
        return
    for i in range(1, n):
        A[0][i] += A[0][i - 1]
    for i in range(1, m):
        A[i][0] += A[i - 1][0]
    for i in range(1, m):
        for j in range(1, n):
            A[i][j] += min(A[i - 1][j], A[i][j - 1])
    return A[-1][-1]
