# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.insert(root,val,root)
    def insert(self,root,val,head):
        if(root.val > val and root.left is None):
            root.left = TreeNode(val)
        if(root.val < val and root.right is None):
            root.right = TreeNode(val)
        if(root.val > val and root.left is not None):
            self.insert(root.left,val,head)
        if(root.val < val and root.right is not None):
            self.insert(root.right,val,head)
        return head
