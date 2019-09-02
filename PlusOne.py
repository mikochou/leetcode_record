#首先想到把数组转换为字符串和整数操作
def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''.join(str(i) for i in digits)
        s1 = int(s)+1
        s,res = str(s1), []
        for i in s:
            res.append(i)
        return res

#第二种方法，在数组上直接操作
def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)-1
        while digits[l] == 9:
            digits[l] = 0
            l-=1
        if l<0: digits = [1]+digits
        else: digits[l] += 1
        return digits
            