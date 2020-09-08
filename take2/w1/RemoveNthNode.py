# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fakeHead=ListNode(0)
        fakeHead.next=head
        
        h1=h2=fakeHead
        
        for i in range(n): 
            h1=h1.next
            
        while h1.next:
            h1=h1.next
            h2=h2.next
            
        h2.next=h2.next.next
        
        return fakeHead.next
                
            