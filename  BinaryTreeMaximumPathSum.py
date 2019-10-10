#对一个node来说，最大经过路径的值为左子树最大路径+node.val+右子树最大路径
#一开始把res设置为0，发现没办法handle节点的值为负的情况
def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node: return 0
            l,r = dfs(node.left), dfs(node.right)
            v = max(node.val, node.val+max(l,r))
            self.res = max(self.res,v,l+r+node.val)
            return v
        self.res = None
        dfs(root)
        return self.res