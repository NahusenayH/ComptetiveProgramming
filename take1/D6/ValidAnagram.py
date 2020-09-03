class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = False
        s = sorted(s)
        t = sorted(t)
        if(s==t):
            res = True
        return res
