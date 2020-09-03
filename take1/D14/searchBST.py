# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.search(root,val)
    def search(self,root,val):
        if(not root):
            return None
        if(root.val == val):
            return root
        left=self.search(root.left,val)
        right=self.search(root.right,val)
        return left if left != None else right