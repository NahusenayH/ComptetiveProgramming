class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = []
        counted = []
        for i in arr:
            if i not in counted:
                counts.append(arr.count(i))
                counted.append(i)
        print(counts)
        for i in range(len(counts)):
            for j in range(len(counts)):
                if i != j :
                    if counts[i] == counts[j]:
                        return False
        return True
        