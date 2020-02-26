class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(1,n//2+1):
            ans.append(-1*i)
            ans.append(i)
        if len(ans) < n:
            ans.append(0)
        return ans
        