import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sumd = 0
        i = 2.0
        if (num == 1):
            return False
        while num > 0 and i <= math.sqrt(num):
            if(num % i == 0):
                if(num/i == i):
                    sumd += i
                else:
                    sumd += i + num/i
            i += 1
        sumd = int(sumd) + 1
        return sumd == num
