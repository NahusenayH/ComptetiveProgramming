# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        total = 0
        def inOrder(node):
            nonlocal total
            if node:
                inOrder(node.left)
                total += node.val
                inOrder(node.right)
        inOrder(root)
        
        mod, res = 10**9 + 7, 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            l, r = dfs(node.left), dfs(node.right)
            res =  max(res, l * (total - l), r * (total - r))
            return l + r + node.val
        
        dfs(root)
        return res % mod
        