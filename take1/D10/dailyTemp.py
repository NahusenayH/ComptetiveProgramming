class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0 for i in range(len(T))]
        stack = []
        for i in range(len(T)-1,-1,-1):
            if stack == []:
                stack.append(i)
            else:
                while stack and T[stack[-1]] <= T[i]:
                    stack.pop()
                result[i] = stack[-1]-i if stack != [] else 0
                stack.append(i)
        return result
