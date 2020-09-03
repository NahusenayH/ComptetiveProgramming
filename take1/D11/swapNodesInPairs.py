# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        temp = head
        if temp is None:
            return
        while temp is not None and temp.next is not None:
            temp.val, temp.next.val = temp.next.val, temp.val
            temp = temp.next.next
        return head