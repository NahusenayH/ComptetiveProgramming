class Solution:
    def reverse(self, x: int) -> int:
        neg = 1
        if(x<0):
            neg = -1
            x = -1 * x
        rem = 0
        while(x>0):
            rem *= 10
            rem += x % 10
            x //= 10
        if(rem > 2147483647 or rem < -2147483647):
            rem = 0
        return neg*rem
