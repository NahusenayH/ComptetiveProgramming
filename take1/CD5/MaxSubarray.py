class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        prev = 0
        ans = nums[0]
        for i in range(len(nums)):
            temp = 0
            if prev > 0:
                temp = prev
            curr = nums[i]+ temp
            prev = curr
            ans = max(ans,curr)
        return ans