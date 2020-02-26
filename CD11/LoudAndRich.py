class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        m = collections.defaultdict(list)
        for i, j in richer:
            m[j].append(i)

        res = [-1] * len(quiet)

        def dfs(i):
            if res[i] > 0: return res[i]
            res[i] = i
            for j in m[i]:
                if quiet[res[i]] > quiet[dfs(j)]:
                    res[i] = res[j]
            return res[i]

        for i in range(len(quiet)):
            dfs(i)
        return res