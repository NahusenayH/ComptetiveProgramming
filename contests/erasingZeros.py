tests = int(input())
cases = []
for i in range(tests):
    temp = input()
    cases.append(temp)
 
for j in range(len(cases)):
    first1 = False
    stack = []
    length = 0
    for k in range(len(cases[j])):
        if cases[j][k] == '1':
            first1 = True
        if first1 and cases[j][k] == '0':
            stack.append('0')
        if first1 and cases[j][k] =='1' and len(stack) > 0:
            length += len(stack)
            stack = []
    print(length)