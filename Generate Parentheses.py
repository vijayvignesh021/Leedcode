class Solution:
    def Parenthesis(self,n, Open, close, s, ans):

        if Open == n and close == n:
            ans.append(s)
            return

        if Open < n:
            self.Parenthesis(n, Open + 1, close, s + "(", ans)

        if close < Open:
            self.Parenthesis(n, Open, close + 1, s + ")", ans)


    def generateParenthesis(self, n: int) -> List[str]:

        ans =[]
        self.Parenthesis(n,0,0,"",ans)
        return ans
