# 遇到单行注释直接跳过，遇到多行注释，使用一个变量来存储状态，如果不是以上两种情况就把字符加入字符串。
def removeComments(self, source):
    """
    :type source: List[str]
    :rtype: List[str]
    """
    res, m = [], False
    line = ''
    for s in source:
        i = 0
        while i < len(s):
            if not m:
                if s[i] == '/' and i < len(s) - 1 and s[i + 1] == '/':
                    break
                elif s[i] == '/' and i < len(s) - 1 and s[i + 1] == '*':
                    m = True
                    i += 1
                else:
                    line += s[i]
            else:
                if s[i] == '*' and i < len(s) - 1 and s[i + 1] == '/':
                    m = False
                    i += 1
            i += 1
        if not m and line:
            res.append(line)
            line = ''
    return res
