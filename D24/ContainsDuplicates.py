class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set([])
        for i in range(len(nums)):
            if i > k:
                window.discard(nums[i-k-1])
            if nums[i] in window:
                return True
            else:
                window.add(nums[i])
        return False