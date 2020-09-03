def pancakeSort (self, A: List[int])->List[int]:
    def flip(A,idx):
        i,j = 0, idx
        while i < j:
            A[i], A[j] = A[j], A[i]
             i += 1
             j -= 1
    res = []
    n = len(A)
    largest = n
    for i in range (n):
        idxLargest = A.index(largest)
        flip(A,idxLargest)
        res.append(idxLargest + 1)
        flip(A,largest)
        res.append(largest)
        largest -= 1
    

    return res