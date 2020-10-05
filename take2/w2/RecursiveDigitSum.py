#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    s = str(n)
    
    while len(s) > 1:
        tempsum = 0
        for i in s:
            tempsum+= int(i)
        s = str(tempsum)
    s = s * k
    while len(s) > 1:
        tempsum = 0
        for i in s:
            tempsum+= int(i)
        s = str(tempsum)
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
