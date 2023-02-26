class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        out = 0
        pre = []
        i = 0
        while (i < len(s)):
            if s[i] =='(':
                pre.append(out)
                out = 0
            else:
                out = pre.pop() + max(1,out *2)
            i += 1

        return out
