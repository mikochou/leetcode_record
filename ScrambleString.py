# 虽然是hard的题，但是蛮简单的，考虑两种情况
# s1的[0:i]和s2[0:i]作为左子树，s1[i:N]和s2[i:N]作为右子树
# s1的[0:i]和s2[N - i:N]作为左子树，s1的[i:N]和s2[0:N-i]作为右子树


def isScramble(self, s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    N = len(s1)
    if N == 0:
        return True
    if N == 1:
        return s1 == s2
    if sorted(s1) != sorted(s2):
        return False
    for i in xrange(1, N):
        if self.isScramble(s1[i:], s2[i:]) and self.isScramble(s1[:i], s2[:i]):
            return True
        elif self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
            return True
    return False
