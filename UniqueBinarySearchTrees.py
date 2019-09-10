# 可以用递归，但这里使用动态规划，状态转移方程为dp[n]=dp[0]dp[n-1]+dp[1]dp[n-2]+......+dp[n-1]*dp[0]
def numTrees(self, n):
    """
    :type n: int
    :rtype: int
    """
    res = [0] * (n + 1)
    res[0] = 1
    for i in xrange(1, n + 1):
        for j in xrange(1, i + 1):
            res[i] += res[j - 1] * res[i - j]
    return res[-1]
