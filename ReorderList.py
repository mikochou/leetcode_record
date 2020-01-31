#找到中心点将链表分为两个部分，将后一部分reverse，然后插入

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pre, node = None, slow
        while node:
            pre, node.next, node = node, pre, node.next
            first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        return
