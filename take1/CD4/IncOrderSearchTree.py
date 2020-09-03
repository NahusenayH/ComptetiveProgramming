# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        lis = []
        def insertInorder(node):
            if node:
                insertInorder(node.left)
                lis.append(node.val)
                insertInorder(node.right)
        insertInorder(root)
        t1 = TreeNode(lis[0])
        temp = t1
        if len(lis) > 0:
            for i in range(1,len(lis)):
                t1.right = TreeNode(lis[i])
                t1 = t1.right
        return temp