class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        final = []
        count = [0 for i in range(1001)]
        for i in arr1:
            count[i] += 1
        for j in arr2:
            occur = count[j]
            final += occur * [j]
            count[j] = 0
        for k in range(len(count)):
            if(count[k]>0):
                final += count[k] * [k]
        return final
