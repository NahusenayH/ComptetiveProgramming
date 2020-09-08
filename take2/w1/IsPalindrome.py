# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        listHead = []
        while head != None:
            listHead.append(head.val)
            head = head.next
        start = 0
        end = len(listHead) - 1
        while start <= end:
            if listHead[start] != listHead[end]:
                return False
            else:
                start += 1
                end -= 1
        return True