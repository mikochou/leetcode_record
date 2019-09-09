#BST中序遍历应该是递增的，利用这个性质来找出错误的节点
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.pre, self.first, self.second = None, None, None
        self.helper(root)
        self.first.val, self.second.val = self.second.val, self.first.val
    
    def helper(self,root):
        if not root: return
        self.helper(root.left)
        if self.pre and self.pre.val>root.val:
            if not self.first:
                self.first=self.pre
            self.second=root
        self.pre = root
        self.helper(root.right)