# 建一个哈希表，存储每个num的最大序列，如果本身包含在一个序列里就删除
def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dic, maxl = set(nums), 0
    for n in set(nums):
        cur, r = 1, n + 1
        while r in dic:
            cur += 1
            dic.remove(r)
            r += 1
        l = n - 1
        while l in dic:
            cur += 1
            dic.remove(l)
            l -= 1
        maxl = max(maxl, cur)
    return maxl

# 讨论里看到的简洁的写法


def longestConsecutive(self, nums):
    nums = set(nums)
    best = 0
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1
            best = max(best, y - x)
    return best
