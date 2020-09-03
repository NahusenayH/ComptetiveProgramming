class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        res = 0
        low,high = 1,1000000
        while low <= high:
            mid = (low + high)//2
            count = 0
            for i in nums:
                count += (i//mid)
                if i%mid != 0:count += 1
            if count <= threshold:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res