# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        if root == None:
            return []
        result = []
        self.postorderTraversalRec(root, result)
        return result
    
    def postorderTraversalRec(self, root, result):
        if root:
            self.postorderTraversalRec(root.left, result)
            self.postorderTraversalRec(root.right, result)
            result.append(root.val)