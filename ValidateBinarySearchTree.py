#判断一棵二叉树树是否是搜索二叉树，BST的特征是中序遍历递增，即left<root<right
def isValidBST(self, root,floor=float('-inf'), ceiling=float('inf')):
        if not root:
            return True
        if root.val <= floor or root.val >= ceiling:
            return False
        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)