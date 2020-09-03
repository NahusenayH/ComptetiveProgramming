import collections
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0
        dominoes = map(tuple,map(sorted,dominoes))
        countedDominoes = collections.Counter(dominoes)
        for key, val in countedDominoes.items():
            count += val * (val-1)/2
        return int(count)