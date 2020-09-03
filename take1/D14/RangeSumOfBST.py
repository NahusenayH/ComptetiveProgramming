# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        rangeSum = self.adder(root,L,R)
        return rangeSum
    
    def adder (self, root,L,R):
        if (root.val>=L and root.val<=R):
            summ = root.val
        else:
            summ = 0
        if(root.left !=None and root.val >= L):
            summ += self.adder(root.left,L,R)
        if(root.right != None and root.val <= R):
            summ += self.adder(root.right,L,R)
        return  summ
        
