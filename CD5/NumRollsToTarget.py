class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10**9 + 7
        mem = [[0]*(target + 1) for _ in range(d + 1)]
        mem[0][0] = 1
        for i in range(1, d + 1):
            for j in range(1, f + 1):
                for k in range(j, target + 1):
                    mem[i][k] = (mem[i][k] + mem[i-1][k-j]) % mod
        return mem[-1][-1]