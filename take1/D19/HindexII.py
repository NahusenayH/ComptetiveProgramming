class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        l, r = 0, N - 1
        H = 0
        while l <= r:
            mid = l + (r - l) // 2
            H = max(H, min(citations[mid], N - mid))
            if citations[mid] < N - mid:
                l = mid + 1
            else:
                r = mid - 1
        return H