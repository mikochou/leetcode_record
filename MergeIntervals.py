
#先将区间按照start来排序
#判断一个区间的start值是否处在前一个区间中
class Solution(object):
    def merge(self, S):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        S.sort(key = lambda i: i.start)
        for s in S:
            if len(res) != 0 and res[-1]<=s.start<=res[-1].end:
                node = res.pop()
                res.append(Interval(node.start,max(node.end,s.end)))
            else:
                res.append(s)
        return res
