class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        
        ans = 1
        temp = 1
        temp1 = 1
            
        for i in range(1,len(A)):
            if A[i] > A[i-1]:
                temp = temp1 + 1
                temp1 = 1
            elif A[i] < A[i-1]:
                temp1 = temp + 1
                temp = 1
            else:
                temp = 1
                temp1 = 1
        ans = max(ans,temp,temp1)
        return ans
    

        