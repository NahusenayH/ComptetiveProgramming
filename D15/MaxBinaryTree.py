# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        maxN = max(nums)
        max_pos = nums.index(maxN)
        root = TreeNode(maxN)
        root.left = self.constructMaximumBinaryTree(nums[:max_pos])
        root.right = self.constructMaximumBinaryTree(nums[max_pos + 1:])
        return root