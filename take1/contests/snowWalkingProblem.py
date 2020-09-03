amt = int(input())
initWalk = []

for i in range(amt):
    snglwalk = input()
    initWalk.append(snglwalk)
for i in initWalk:
    lcount = i.count("L")
    rcount = i.count("R")
    ucount = i.count("U")
    dcount = i.count("D")
    lcount = rcount = min(lcount,rcount)
    ucount = dcount = min(ucount,dcount)
    ans = ""
    if(ucount == 0 and lcount > 0):
        lcount = rcount = 1
    if(ucount > 0 and lcount == 0):
        ucount = dcount = 1
    for i in range(ucount):
        ans += "U"
    for i in range(rcount):
        ans += "R"
    for i in range(dcount):
        ans += "D"
    for i in range(lcount):
        ans += "L"
    print(len(ans))
    print(ans)