# 主要是终止条件的取值，left>ri
def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        return self.dfs(1, n)

    def dfs(self, left, right):
        if left > right: return [None]
        res = []
        for i in range(left, right+1):
            lefts = self.dfs(left,i-1)
            rights = self.dfs(i+1, right)
            for l in lefts:
                for r in rights:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res
