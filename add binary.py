class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ""
        while a or b or carry:
            out = carry
            if a:
                out += int(a[-1])
                a = a[0:len(a)-1]
            if b :
                out += int(b[-1])
                b = b[0:len(b)-1]
            carry = out // 2
            res += str(out % 2)
        return res[::-1]
