# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None:        return None
        temp = ListNode(-1)       
        temp.next = head
        current = head.next            
        head.next = None               
        sortedEnd = head                
        while current != None:
            nextCurrent = current.next
            if sortedEnd.val <= current.val:
                sortedEnd.next = current
                current.next = None
                sortedEnd = current
            else:
                headOfSorted = temp
                while headOfSorted.next.val < current.val:
                    headOfSorted = headOfSorted.next
                current.next = headOfSorted.next
                headOfSorted.next = current
            current = nextCurrent
        return temp.next