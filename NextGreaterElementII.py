# 需要遍历两次，用栈来记录值
def nextGreaterElements(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    l = len(nums)
    res = [-1] * l
    stack = []
    for i in range(l) * 2:
        while stack and nums[stack[-1]] < nums[i]:
            res[stack.pop()] = nums[i]
        stack.append(i)
    return res
