# 翻转90度，不能使用额外的空间。
    l = len(A)
    for i in range(l):
        for j in range(i + 1, l):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    for i in range(l):
        A[i] = A[i][::-1]

# one-liner
    A[:] = zip(*A[::-1])
