# import collections
# arr = [[2,3],[3,2],[2,1],[3,4],[1,2]]

# arr = map(tuple, map(sorted, arr))
# print(arr)
# d = collections.Counter(arr)
# print(d)
# res = 0
# for key , v in d.items():
#     res += v * (v - 1) / 2
# print(res)


inc = False
dec = False
a = [1,2,3]
inc = all(a[i]<=a[i+1] for i in range(len(a)-1))
dec = all(a[i]>=a[i+1] for i in range(len(a)-1))
print(inc)
print(dec)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    lis = []
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.insertToList(root)
        self.lis = sorted(self.lis)
        t1.
        
    def insertToList(self,node):
        if node is not None:
            self.lis.append(node.val)
            self.insertToList(node.right)        
            self.insertToList(node.left)

        