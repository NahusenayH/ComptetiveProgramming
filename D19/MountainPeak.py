class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left, right = 0, len(A)-1
        while left < right:
            mid = left + (right - left) // 2
            if A[mid - 1] < A[mid] and A[mid] > A[mid + 1]:
                return mid
            if A[mid] < A[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return -1