"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        maxDepth = 1
        for i in root.children:
            temp = 1 + self.maxDepth(i)
            if temp > maxDepth:
                maxDepth = temp
        return maxDepth
            
        