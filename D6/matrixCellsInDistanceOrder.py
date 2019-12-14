class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        matrix = []
        distance = []
        combined = dict()
        for i in range(R):
            for j in range(C):
                matrix.append([i,j])
        for k in matrix:
                tempdis = abs(k[0]-r0)+abs(k[1]-c0)
                distance.append(tempdis)
                if matrix[tempdis] == None:
                    matrix[tempdis] =[k]
                else:
                    matrix[tempdis]=matrix[tempdis].append(k)
        distance, matrix = zip(*sorted(zip(distance, matrix)))
        return matrix
