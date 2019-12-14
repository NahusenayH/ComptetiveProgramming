class Solution:
    def isValid(self, s: str) -> bool:
        openB = ["[","{","("] 
        closeB = ["]","}",")"]  
        stack = []
        for i in s:
            if i in openB:
                stack.append(i)
            elif i in closeB:
                indx = closeB.index(i)
                if((len(stack)>0) and (openB[indx]== stack[-1])):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
