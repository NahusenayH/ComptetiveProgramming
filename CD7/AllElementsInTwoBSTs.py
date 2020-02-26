# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        lis = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            lis.append(node.val)
            inorder(node.right)
        inorder(root1)
        inorder(root2)
        lis = sorted(lis)
        return lis
        