class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lis = []
        for i in nums1:
            if i in nums2:
                if i not in lis:
                    lis.append(i)
        return lis
