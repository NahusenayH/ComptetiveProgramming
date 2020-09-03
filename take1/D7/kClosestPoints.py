import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance = []
        for i in points:
            distance.append(math.sqrt(abs(i[0])**2+abs(i[1])**2))
        distance, points = zip(*sorted(zip(distance, points)))
        return points[0:K]
        
