# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        node_list = []
        while head:
            node_list.append(head)
            head = head.next
        if k < 1 or k > len(node_list):
            return
        return node_list[-k]
