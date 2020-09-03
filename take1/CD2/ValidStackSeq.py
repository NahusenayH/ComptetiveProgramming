class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popIdx = 0
        for i in pushed:
            stack.append(i)
            while popIdx < len(popped):
                if len(stack) <=0 or popped[popIdx] != stack[-1]:
                    break
                stack.pop()
                popIdx +=1
        return popIdx == len(popped)