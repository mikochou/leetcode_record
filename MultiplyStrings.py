# 需要先翻转两个数，按位相乘，注意每一位上的求余和进位。
    res = [0] * (len(num1) + len(num2))
    for i, v1 in enumerate(reversed(num1)):
        for j, v2 in enumerate(reversed(num2)):
            int1 = ord(v1) - ord('0')
            int2 = ord(v2) - ord('0')
            res[i + j] += int1 * int2
            res[i + j + 1] += res[i + j] // 10
            print res[i + j], res[i + j + 1]
            res[i + j] %= 10
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return ''.join(str(v) for v in res)[::-1]
