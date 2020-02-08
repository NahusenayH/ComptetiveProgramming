class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        firstIdx = 0
        while (firstIdx+k) <= len(s):
            remove = s[firstIdx:firstIdx+k]
            dup = remove[0]*k
            if dup == remove:
                s = s[0:firstIdx] + s[firstIdx+k:]
                firstIdx = 0
                continue
            firstIdx += 1
        return s