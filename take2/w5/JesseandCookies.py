#!/bin/python3

import os
import sys
import heapq
#
# Complete the cookies function below.
#
def cookies(k, A):
    #
    # Write your code here.
    #
    heapq.heapify(A)
    operations = 0
    try:
        while A[0] < k:
            sweetness = heapq.heappop(A) + 2 * heapq.heappop(A)
            heapq.heappush(A, sweetness)
            operations += 1
    except IndexError:
        return -1
    return operations
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
