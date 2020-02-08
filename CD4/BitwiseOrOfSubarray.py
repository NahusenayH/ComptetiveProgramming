class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans = set()
        subArrVal = set()
        for a in A:
            subArrVal = {i | a for i in subArrVal} | {a}
            ans |= subArrVal
        print(ans)
        print(subArrVal)
        return len(ans)
        