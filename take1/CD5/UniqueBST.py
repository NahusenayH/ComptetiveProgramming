class Solution:
    dp = dict()
    def numTrees(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        if n== 0 or n ==1:
            return 1
        ans = 0 
        for i in range(1, n+1):
            ans += self.numTrees(i-1) * self.numTrees(n-i)
        self.dp[n] = ans
        return ans
        