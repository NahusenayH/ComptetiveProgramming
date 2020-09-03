class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0 for i in range (3)]
        for   i in nums:
            count[i] += 1
        nums.clear()
        for j in range(3):
            if (count[j]>0):
                nums += count[j] * [j]
