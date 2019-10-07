# 先在先序遍历中找到根节点，再在中序遍历中找到左右节点
def buildTree(self, preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    if not preorder or not inorder:
        return None

    rootValue = preorder.pop(0)
    root = TreeNode(rootValue)
    inorderIndex = inorder.index(rootValue)

    root.left = self.buildTree(preorder, inorder[:inorderIndex])
    root.right = self.buildTree(preorder, inorder[inorderIndex + 1:])

    return root
