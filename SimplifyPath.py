#简化路径，把字符提取出来，再转化成路径的形式
def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path.replace('//','/')
        temp = path.split('/')
        res = []
        for i in range(len(temp)):
            if temp[i] == '..' and len(res) > 0:
                res.pop()
            elif temp[i] != '' and temp[i] != '.' and temp[i] != '..':
                res.append(temp[i])
        return '/'+'/'.join(res)