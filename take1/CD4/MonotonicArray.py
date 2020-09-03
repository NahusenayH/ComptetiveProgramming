class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc = all(A[i]<= A[i+1] for i in range(len(A)-1))        
        dec = all(A[i]>= A[i+1] for i in range(len(A)-1))
        if inc or dec:
            return True
        return False