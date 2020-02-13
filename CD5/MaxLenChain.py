class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort( key=lambda x: x[1])
        curr = float('-inf')
        ans = 0
        for x, y in pairs:
            if curr < x:
                curr = y
                ans += 1
        return ans
#  
#