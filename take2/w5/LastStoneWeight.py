class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if stones == None:
            return
        while len(stones) > 1:
            max1 = max(stones)
            stones.pop(stones.index(max1))            
            max2 = max(stones)
            stones.pop(stones.index(max2))
            stones.append(max1-max2)
        return stones[0]