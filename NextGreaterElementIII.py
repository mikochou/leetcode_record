# 从后往前找到第一个降序的数字，把此位置后面的翻转，再把这个降序数字和后面第一个比它大的位置交换。
def nextGreaterElement(self, n):
    """
    :type n: int
    :rtype: int
    """
    s = list(str(n))
    i = len(s) - 1

    while i - 1 >= 0 and s[i - 1] >= s[i]:
        i -= 1

    if i == 0:
        return -1
    j = len(s) - 1
    while s[j] <= s[i - 1]:
        j -= 1
    s[i - 1], s[j] = s[j], s[i - 1]
    s[i:] = s[i:][::-1]
    res = int(''.join(s))
    if res <= 2**31 - 1:
        return res
    return -1
