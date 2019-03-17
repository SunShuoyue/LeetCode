# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head
        elif head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
            return head
        else:
            head = head.next
            head = self.deleteDuplicates(head)
            return head

