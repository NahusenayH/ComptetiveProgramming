# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0        
        def trav(root):
            if not root :
                return 0
            left = trav(root.left)
            right = trav(root.right)
            self.ans += abs(left) + abs(right)
            return root.val - 1 + left +right
        trav(root)
        return self.ans
        