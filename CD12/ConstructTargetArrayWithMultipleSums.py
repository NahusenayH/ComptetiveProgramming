class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) <= 1 and target[0] != 1:
            return False
        if len(target) == 1 and target[0] == 1:
            return True
        heap = []
        for i in target:
            heap.append(-i)
        heapq.heapify(heap)
        total = sum(target)
        while True:
            a = -heapq.heappop(heap)
            total -= a
            if a == 1 or total == 1: 
                return True
            if a < total or a % total == 0:
                return False
            a %= total
            total += a
            heapq.heappush(heap, -a)