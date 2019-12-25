import math
tests = int(input())
lisTest = list()
for i in range(tests):
    singleTest = input().split(" ")
    singleTest[0] = int(singleTest[0])
    singleTest[1] = int(singleTest[1])
    singleTest[2] = int(singleTest[2])
    lisTest.append(singleTest)    
for k in lisTest:
    distance = []
    x = [k[0], k[0]-1,k[0]+1]
    y = [k[1], k[1]-1,k[1]+1]
    z = [k[2], k[2]-1,k[2]+1]
    for l in range(3):
        for m in range(3):
            for n in range(3):
                tempdis = abs(x[l]-y[m]) + abs(x[l]-z[n]) + abs(y[m]-z[n])
                distance.append(tempdis)
    print(min(distance))