class Solution:
    def evalRPN(self, tokens: List[str])->int:
        result = 0
        items = []

        for i in tokens:
            try:
                int(i)
                isNum = True
            except:
                 isNum = False
            if isNum:
                items.append(int(i))
            if not isNum:
                x = items.pop()
                y = items.pop()
                operator = i
                if operator == "+":
                    result = x + y
                    items.append(result)
                if operator == "-":
                    result = x - y
                    items.append(result)
                if operator == "*":
                    result = x * y
                    items.append(result)
                if operator == "/":
                    result = x / y
                    items.append(result)
        return result
                    