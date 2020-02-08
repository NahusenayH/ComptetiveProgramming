class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = [0] * (len(cost)+1)
        ans[0] = cost[0]
        ans[1] = cost[1]
        cost.append(0)
        for i in range(2,len(cost)):
            ans[i] = min(ans[i-1], ans[i-2]) + cost[i]
        return ans[-1]