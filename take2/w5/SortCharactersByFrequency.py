class Solution:
    import collections
    def frequencySort(self, s: str) -> str:
        freq = collections.Counter(s)
        freq = sorted(freq.items(), key=lambda x: (x[1],x[0]), reverse=True)
        ans = []
        for i in range(len(freq)):
            ans.append(freq[i][0] * freq[i][1])
        return "".join(ans)
        