class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for i in A:
            if(i%2 == 0):
                even.append(i)
            elif(i%2!=0):
                odd.append(i)

        for i in range(len(A)):
            if(i%2 == 0):
                A[i] = even.pop()
            elif(i%2!=0):
                A[i] = odd.pop()
        return A
        
