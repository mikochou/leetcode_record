# 动态规划，从当前位置i回看仅查找子串并在dp [ j ] == true的后一位置查找字典。
def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(len(s)):
        if dp[i]:
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict:
                    dp[j + 1] = True
    return dp[-1]
