class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        s = []
        while root and (root.left or root.right or s):
            if root.right:
                s.append(root.right)
                root.right = None
            if root.left:
                root.right, root.left = root.left, None
                root = root.right
            elif s:
                root.right = s.pop()
                root = root.right
