class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        perimeter = 0
        A.sort()
        A.reverse()
        i=0
        j=1
        k=2
        for i in range(len(A)):
            if(j<len(A) and k<len(A)):
                if((A[i]+A[j]>A[k]) and (A[i]+A[k]>A[j]) and (A[k]+A[j]>A[i])):
                    if(A[i]+A[j]+A[k] >= perimeter):
                        perimeter =A[i]+A[j]+A[k]
            j+=1
            k+=1 
        return perimeter
