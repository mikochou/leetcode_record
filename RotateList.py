# 其实就是把链表的后k个移到前面去，但k可能大于链表长度，我们需要先求出链表长度l，然后求出最终的步数。
def rotateRight(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not head:
        return None
    p = q = head
    l = 1
    while p.next:
        p = p.next
        l += 1
    p.next = head
    k %= l
    step = abs(l - k - 1)
    for _ in range(step):
        q = q.next
    res = q.next
    q.next = None
    return res
