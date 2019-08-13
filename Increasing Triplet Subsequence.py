#遍历数组，保存最小和次小的数。
#感觉不像medium难度的题
        l,r=float('inf'),float('inf')
        for n in nums:
            if n<=l: l=n
            elif n<=r: r=n
            else: return True
        return False