# 格雷码的公式i^(i>>1)，自己与自己右移一位进行异或
def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [(i >> 1) ^ i for i in xrange(2**n)]

# 另外一个递归的解法


def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        temp = self.dfs(n)
        for n in temp:
            res.append(int(n, 2))
        return res

    def dfs(self,n):
        res = None
        if n==0: res = ['0']
        elif n==1: res = ['0','1']
        else:
            pre = self.dfs(n-1)
            res = ['0'+x for x in pre] + ['1'+ x for x in pre[::-1]]
        return res
