class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        # added = []
        # diff = []
        # for idx,val in enumerate(arr):
        #     added.append(val + idx)
        #     diff.append(val - idx)
        a, b, c, d = [], [], [], []
        for i in range(len(arr1)):
            x, y = arr1[i], arr2[i]
            a.append(x + y + i)
            b.append(x + y - i)
            c.append(x - y + i)
            d.append(x - y - i)
            
        ans1 = max(a) - min(a)
        ans2 = max(b) - min(b)
        ans3 = max(c) - min(c)
        ans4 = max(d) - min(d)
        
        return max(ans1, ans2, ans3, ans4)