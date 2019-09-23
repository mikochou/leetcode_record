# 使用一个单调递增栈来维护已经出现了的矩形高度，如果后面新来的元素高度比栈里最后的元素高，那么需要入栈
def largestRectangleArea(self, A):
    """
    :type heights: List[int]
    :rtype: int
    """
    stack, res, lens = [], 0, len(A) + 1
    A.append(0)
    for i in range(lens):
        if not stack or A[i] > A[stack[-1]]:
            stack.append(i)
        else:
            while stack and A[i] <= A[stack[-1]]:
                h = A[stack[-1]]
                stack.pop()
                wid = i if not stack else i - stack[-1] - 1
                res = max(res, h * wid)
            stack.append(i)
    return res
