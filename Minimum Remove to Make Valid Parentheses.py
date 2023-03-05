class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sym = []
        index = []
        s = list(s)
        for inx , ch  in enumerate(s):
            if ch == '(':
                sym.append('(')
                index.append(inx)
            elif ch == ')':
                if len(sym) > 0 and sym[-1] == '(':
                    sym.pop()
                    index.pop()
                else:
                    sym.append(')')
                    index.append(inx)
        print(sym , index)
        for i in index:
            s[i] =""

        return "".join(s)
