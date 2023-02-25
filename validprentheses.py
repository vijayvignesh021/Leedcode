class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = [ '[' , '(' , '{' ]
        for i in range(len(s)):
            if s[i] in opens :
                stack.append(s[i])
            elif stack :
                if s[i] == "]" and stack[-1] == '[':
                    stack.pop()
                elif s[i] == ')' and stack[-1] == '(':
                    stack.pop()
                elif s[i] == '}' and stack[-1] == '{':
                    stack.pop()
                else :
                    return False
            else :
                return False 
        if len(stack) == 0:
            return True    
        return False
