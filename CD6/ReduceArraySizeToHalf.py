import math
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = []
        redSize = 0
        length = 0
        for i in range(len(arr)):
            counts.append(arr.count(arr[i]))
        counts = [x for x in reversed(sorted(counts))]
        print(counts)
        half =len(arr)//2
        for j in range(len(counts)):
            if redSize >= half:
                return j+1
            else:
                redSize += counts[j]
                length += 1
        return length