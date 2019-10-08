# 把链表转换为二叉搜索树，其实就是根据中序遍历序列建造二叉树，利用快慢指针的方法找到中点
def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: return head
        if not head.next: return TreeNode(head.val)
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.next.val)
        root.right = self.sortedListToBST(slow.next.next)
        slow.next = None
        root.left = self.sortedListToBST(dummy.next)
        return root

# 把链表转换为数组


def sortedListToBST(self, head):
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        return self.sortedArrayToBST(ls)

    def sortedArrayToBST(self, num):
        if not num:
            return None

        mid = len(num) // 2

        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])

        return roo
