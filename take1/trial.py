def saveRequestBytime(starttime, id, endtime):
    newline = starttime+" " + id+" " + endtime+"\n"
    f = open("t.txt","r+",encoding='utf-8')
    f1 = f.readlines()
    print(f1)
    f1.append(newline)
    f1 = sorted(f1)
    print(f1)
    for i in f1:
        f.write(i)
    f.close()

saveRequestBytime("10:02", "3", "10:50")
