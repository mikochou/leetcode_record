#只反向m-n，设计一个dummy存储前面不用反向的节点，反向之后链接起来
def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        p=dummy=ListNode(0)
        dummy.next = head
        for _ in range(m-1):
            p=p.next
        cur,pre = p.next,None
        for _ in range(n-m+1):
            cur.next,pre,cur = pre,cur,cur.next
        p.next.next = cur
        p.next = pre
        
        return dummy.next