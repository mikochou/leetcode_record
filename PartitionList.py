#用两个指针记录比x大的部分和小的部分，遍历完后拼接起来    
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None or x is None:
            return head
        p1=head1=ListNode(0)
        p2=head2=ListNode(0)
        p=head
        
        while p:
            if p.val<x:
                p1.next=p
                p1=p1.next
            else:
                p2.next=p
                p2=p2.next
            p=p.next
        p1.next=head2.next
        p2.next=None
        return head1.next