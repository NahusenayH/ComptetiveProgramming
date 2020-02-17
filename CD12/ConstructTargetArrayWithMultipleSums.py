class Solution:
    def isPossible(self, target: List[int]) -> bool:
        maxi = max(target)
        ans = maxi - (sum(target)-maxi)
        while ans >= 1:
            maxi = max(target)
            ans = maxi - (sum(target)-maxi)
            if ans < 1:
                break
            target[target.index(maxi)] = ans
        finalSum = sum(target)
        print(target)
        return finalSum == len(target)