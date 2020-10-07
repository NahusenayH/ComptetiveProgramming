import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        count = [0] * len(primes)
        res = [0] * n
        res[0] = 1
        for i in range(1,n):
            minm = float(inf)
            for j in range(0,len(primes)):
                minm = float(min(minm,primes[j]*res[count[j]]))
            
            res[i] = int(minm)
            
            for j in range(0,len(count)):
                if ((res[count[j]] * primes[j]) == int(minm)):
                    count[j] += 1
                    
        return res[-1]