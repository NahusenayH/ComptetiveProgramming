# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        return self.merger(t1,t2)
        
    def merger(self, t1, t2):
        if(not t1):
            return t2
        if(not t2):
            return t1
        t1.val += t2.val
        t1.left = self.merger(t1.left,t2.left)
        t1.right = self.merger(t1.right,t2.right)
        return t1
