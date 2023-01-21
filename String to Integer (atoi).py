class Solution:
    def myAtoi(self, s: str) -> int:
        out =""
        mat=["+","-"]
        for _ in s[0:]:
            if _ == " " and out == "":
                continue
            elif (_ == "+" or _ == "-") and out == "":
                out+=_
            elif _.isnumeric():
                out+=_
            else:
                break
        if out == "" or out == "+" or out == "-":
            return 0
        new = int(out)
        if new < -2147483648:
            return -2147483648
        elif new > 2147483647:
            return 2147483647
        return new
