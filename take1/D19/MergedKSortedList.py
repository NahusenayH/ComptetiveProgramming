# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        if all(x is None for x in lists):
            return
        lis = [] 
        heapq.heapify(lis)
        
        def trav(node):
            if node:
                trav(node.next)
                heapq.heappush(lis,node.val)
        
        for i in lists:
            if i:
                trav(i)
            
            
        t1 = ListNode(heapq.heappop(lis))
        temp = t1
        while lis:
            temp.next = ListNode(heapq.heappop(lis))
            temp = temp.next
        return t1