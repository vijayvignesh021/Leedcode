class Solution:
    def win(self,x,k,cur):
        if len(x) == 1:
            return x[0]
        if k+cur-1< len(x):
            x.pop(k+cur-1)
            cur = k+cur-1
        else:
            cur = cur-len(x)
        return self.win(x,k,cur)


    def findTheWinner(self, n: int, k: int) -> int:
        x = [i+1 for i in range(n)]
        cur=0
        return self.win(x,k,cur)
