class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time = time - n +1
        if time > 0:
            z = time//(n-1)
            o = time % (n-1)
            if z%2 != 0:
                return 1 + o
            else:
                return n - o
        else : 
            return time + n
