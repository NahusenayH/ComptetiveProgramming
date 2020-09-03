def compute(op1,op2,oper):
    if(oper=="+"):
        return op1 + op2
    elif(oper=="-"):
        return op1 - op2
    elif(oper=="/"):
        return op1 / op2
    elif(oper=="*"):
        return op1 * op2

first = input().split(" ")
strops = '+-*/'
operators =[]
operands = []
for i in first:
    if i in strops:
        operators.append(i)
    else:
        operands.append(int(i))
while len(operators) > 0:
    op1 = operands.pop()
    op2 = operands.pop()
    oper = operators.pop()
    operands.append(compute(op2,op1,oper))
print("result ",operands[0])