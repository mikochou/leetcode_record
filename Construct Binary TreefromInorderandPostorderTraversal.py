# 在后序遍历中找根，先递归遍历右子树，再递归遍历左子树
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        val = postorder.pop(-1)
        root = TreeNode(val)
        i = inorder.index(val)
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i + 1:], postorder[i:])
        return root

# 前一个方法的复杂度为O(n^2)，将index转化为map


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        map_inorder = {}
        for i, val in enumerate(inorder):
            map_inorder[val] = i

        def recur(low, high):
            if low > high:
                return None
            x = TreeNode(postorder.pop())
            mid = map_inorder[x.val]
            x.right = recur(mid + 1, high)
            x.left = recur(low, mid - 1)
            return x
        return recur(0, len(inorder) - 1)
