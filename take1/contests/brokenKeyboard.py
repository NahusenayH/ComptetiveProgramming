first = input().split(" ")
mainStr = input()
availChars = input().split(" ")
subStrings = set()
for i in mainStr:
    if(i not in availChars):
        mainStr = mainStr.replace(i,"")
for i in range(len(mainStr)):
    for j in range (len(mainStr)):
        subStrings.add(mainStr[i:j])
print(subStrings)