# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.check(p,q)
    def check(self,p, q):
        if (p is None and q is None):
            print("true 1")
            return True
        if (p is not None and q is None):
            print("false 1")
            return False
        if (p is None and q is not None):
            print("false 2")
            return False
        else:
            result= self.check(p.left,q.left) and self.check(p.right,q.right)
            print(result)
            if(p.val == q.val and result):
                print("true 2")
                return True
            else:
                print("false 3")
                return False