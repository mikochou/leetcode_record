#快慢指针相遇在点c，然后令慢指针从head出发，快指针从c点出发，两者相遇即是环的入口
def detectCycle(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    try:
        slow = head.next
        fast = head.next.next
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
    except:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
