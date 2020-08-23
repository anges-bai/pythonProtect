# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def ReverseList(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        pre = None
        cur = pHead
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
