import math
tests = int(input())
cases = []
for i in range(tests):
    temp = input()
    cases.append(temp)

for i in cases:
    j = i.split(" ")
    n = int(j[0])
    g = int(j[1])
    b = int(j[2])
    numbadjump = 0
    minunit = math.ceil(n/2)
    curunit = 0
    minday = 1
    if g >= minunit:
        print (n)
        continue
    while curunit < minunit:
        tempp = curunit + g
        if tempp <= minunit:
            curunit += g
            minday = minday + (g+b-1)
            # numbadjump += b
        if tempp > minunit:
            diff = tempp - minunit
            curunit += diff
            minday = minday + diff#(g-1)
    #         break
    # left = n - curunit
    # if numbadjump < left:
    #     minday += left - numbadjump
    
    print(minday)