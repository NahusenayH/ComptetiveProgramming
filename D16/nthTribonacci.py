class Solution():
    fib_list= []
    def tribonacci(self, n: int) -> int:
        f = [0,1,1]
        if len(self.fib_list) == 0:
            for i in range(0,38):
                if i <= 2:
                    self.fib_list.append(f[i])
                    continue
                self.fib_list.append(self.fib_list[-1] + self.fib_list[-2] + self.fib_list[-3])

        return self.fib_list[n]