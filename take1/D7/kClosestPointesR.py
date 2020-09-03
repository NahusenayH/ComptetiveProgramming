import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance = []
        ans= []
        for i in points:
            distance.append(math.sqrt(abs(i[0])**2+abs(i[1])**2))
        for i in range(K):
            ans.append(points[distance.index(min(distance))])
            distance[distance.index(min(distance))] = min(distance)+max(distance)
        return ans
