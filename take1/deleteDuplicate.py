class Solution:
    def deleteNode(slef, head:ListNode)-> ListNode:
        ans = head
        if not head:
            return head
        while head.next:
            if head.val == head.next.val:
                head.next == head.next.next
            else:
                head = head.next
        return ans