# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        consCount = 0
        temp = head
        G = set(G)
        print(G)
        while temp:
            if temp.val in G and (not temp.next or temp.next.val not in G):
                consCount += 1
            temp = temp.next
        return consCount
        