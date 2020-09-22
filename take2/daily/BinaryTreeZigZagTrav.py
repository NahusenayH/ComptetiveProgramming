# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, node, level, res):
        if node:
            if len(res) < level + 1: 
                res.append([])
            if level % 2 == 0:
                res[level].append(node.val)
            else:
                res[level].insert(0, node.val)
            self.preorder(node.left, level + 1, res)
            self.preorder(node.right, level + 1, res)
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.preorder(root, 0, res)
        return res