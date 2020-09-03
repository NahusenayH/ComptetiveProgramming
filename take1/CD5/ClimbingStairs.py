class Solution:
    dp = [0]*2
    def climbStairs(self, n: int) -> int:
        self.dp[0] = 1
        self.dp[1] = 1
        if n >= len(self.dp):
            for i in range(len(self.dp),n+1):
                self.dp.append(self.dp[i-1]+self.dp[i-2])
        return self.dp[n]