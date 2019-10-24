# 遍历链表两次, 第一次遍历是构造字典的键值对, 第二次遍历时, 将原节点的next和random复制到新节点中.

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dic = dict()
        m = n = head
        while m:
            dic[m] = Node(m.val, None, None)
            m = m.next
        while n:
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next
        return dic.get(head)
