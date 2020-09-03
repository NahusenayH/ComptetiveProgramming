class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        areas = []
        for i in rectangles:
            x = abs(i[0] - i[2])
            y = abs(i[1] - i[3])
            areas.append(x*y)#%((10**9)+7))
        print(areas)
        return sum(areas)