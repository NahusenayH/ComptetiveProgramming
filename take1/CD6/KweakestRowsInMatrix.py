class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        order = [0]*len(mat)
        ordIdx = [0]*len(mat)
        ans = []
        for j in range(len(mat)):
            ordIdx[j] = j
        for i in range(len(mat)):
            order[i] = sum(mat[i])
            
        ordIdx = [x for _,x in sorted(zip(order,ordIdx))]
        
        return ordIdx[:k]
        