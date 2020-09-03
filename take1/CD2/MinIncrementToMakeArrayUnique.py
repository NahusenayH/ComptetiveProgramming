class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A = sorted(A)
        count = 0
        for i in range(1,len(A)):
            if i <len(A):
                if A[i] <= A[i-1]:
                    count+=A[i-1]-A[i]+1
                    A[i] = A[i-1]+1
        return count
                
            
            
            