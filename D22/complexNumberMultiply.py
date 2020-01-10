class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        num1 = list(map(int, a[:-1].split('+')))
        num2 = list(map(int, b[:-1].split('+')))
        
        intPart = num1[0] * num2[0] - num1[1] * num2[1]
        iPart = num1[0] * num2[1] + num1[1] * num2[0]
        return "%d+%di" % (intPart, iPart)