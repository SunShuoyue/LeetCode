# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        prev, cur = None, res
        while l1:
            if l2:
                value = l1.val+l2.val+cur.val
                cur.next = ListNode(value//10)
                cur.val = value%10
                l1 = l1.next
                l2 = l2.next
                prev, cur = cur, cur.next
            else:
                value = l1.val+cur.val
                cur.next = ListNode(value//10)
                cur.val = value%10
                l1 = l1.next
                prev, cur = cur, cur.next
        while l2:
            value = l2.val+cur.val
            cur.next = ListNode(value//10)
            cur.val = value%10
            l2 = l2.next
            prev, cur = cur, cur.next
        if cur.val == 0:
            prev.next = None
        return res