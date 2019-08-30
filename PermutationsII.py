# 给出的nums中有重复数字。
# 一种方法是在前一道题里添加一个判断条件，看最后的path有没有在res中重复。
# 这里只写非递归的方法。
    res = [[]]
    for n in nums:
        temp = []
        for r in res:
            for i in xrange(len(r) + 1):
                temp.append(r[:i] + [n] + r[i:])
                if len(r) > i and r[i] == n:
                    break
            res = temp
    return res
