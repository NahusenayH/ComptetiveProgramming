class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        for p,s in sorted (zip(position,speed)):
            times.append(float(target-p)/s)
        result, curr = 0, 0
        for t in reversed(times):
            if t > curr:
                result += 1
                curr = t
        return result
