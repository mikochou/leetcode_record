#求平方根的整数部分，用二分查找
def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2: return x
        l,r = 1,x/2
        while l<=r:
            m = (l+r)/2
            if x == m*m: return m
            if x > m*m: 
                l = m+1
                res = m
            else: r = m-1
        return res

        
#在讨论中看到的牛顿法
#f(r) = r^2 - x = 0
#r(n+1) = r(n) - f(r(n)) / f'(r(n))
#r(n+1) = (r(n) + x / r(n)) / 2
def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r*r > x:
            r = (r+x/r)/2
        return r
