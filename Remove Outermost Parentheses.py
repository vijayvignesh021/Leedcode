class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stk = 0
        sm = ""
        strs = ""
        i = 0
        while i < len(s):
            if s[i] == ')':
                stk -= 1
                strs += s[i]
            else:
                stk += 1
                strs += s[i]
            if stk == 0:
                sm += strs[1:len(strs)-1]
                strs = ""
            i += 1
        return sm
