class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        out = []
        digits[-1] = digits[-1]+1
        for i in range(len(digits)-1,-1,-1):
            digits[i] = digits[i] + carry
            out.insert(0,digits[i]%10 )
            carry = digits[i]//10
        if carry :
            out.insert(0,carry)
        return out
