# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        car = 0
        added = l1.val + l2.val + car
        if added >= 10:
            car = 1
        else:
            car = 0
        added = added if added < 10 else added % 10
        ans = ListNode(added)
        l1 = l1.next
        l2 = l2.next
        prev = ans
        while ((l1 is not None) or (l2 is not None)):
            if (l1 == None):
                l1=ListNode(0)
            elif(l2 == None):
                l2=ListNode(0)
            added =car + l1.val + l2.val
            if added >= 10:
                car = 1
            else:
                car = 0
            added = added if added < 10 else added % 10
            temp = ListNode(added)
            prev.next = temp
            prev = temp
            l1 = l1.next
            l2 = l2.next
        if car > 0:
            temp = ListNode(car)
            prev.next = temp
            prev = temp
        return ans
