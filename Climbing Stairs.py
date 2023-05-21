class Solution:
    def fact(self,num):
        fact = 1
        for i in range(1, num+1):
            fact = fact * i
        return fact

    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        out = 1 if n%2 == 0 else 0
        twos = 0
        while(n > 0):
            out += self.fact(n+twos)//(self.fact(n) *self.fact(twos))
            n -= 2 
            twos += 1
        return out 
