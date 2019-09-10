# 使用动态规划，状态转移方程为f(i,j) = (s3(i+j)==s1(i)&&f(i-1,j)==true)||(s3(i+j)==s2(j)&&f(i,j-1))


def isInterleave(self, s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    l1, l2, l3 = len(s1), len(s2), len(s3)
    if l1 + l2 != l3:
        return False
    dp = [[False] * (l2 + 1) for i in range(l1 + 1)]
    dp[0][0] = True
    for i in xrange(1, l1 + 1):
        dp[i][0] = (s1[i - 1] == s3[i - 1] and dp[i - 1][0])
    for j in xrange(1, l2 + 1):
        dp[0][j] = (s2[j - 1] == s3[j - 1] and dp[0][j - 1])
    for i in xrange(1, l1 + 1):
        for j in xrange(1, l2 + 1):
            dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                        ) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
    return dp[-1][-1]
