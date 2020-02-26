class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int: 
        ind = -200000
        ans = [0] * len(seats)
        for i in range(len(seats)):
            if seats[i] == 1:
                ind = i
            else:
                ans[i] = abs(i - ind)
        ind = -200000
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                ind = i
            else:
                ans[i] = min(abs(i - ind), ans[i])
        return max(ans)
                