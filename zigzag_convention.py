class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr=["" for i in range(numRows)]
        row = 0
        for i in range(len(s)):
            arr[row] += s[i]
            if row == numRows-1:
                down = False
            elif row == 0:
                down = True
            if down :
                row += 1
            else:
                row -= 1
        return "".join(arr)
