#使用hashmap，保存每个缝隙，然后找竖着方向上最多的那个
def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        hashs = collections.defaultdict(int)
        count = 0
        for row in wall:
            l=0
            for brick in row[:-1]:
                l += brick
                hashs[l] += 1
                count = max(count,hashs[l])
        return len(wall)-count
        