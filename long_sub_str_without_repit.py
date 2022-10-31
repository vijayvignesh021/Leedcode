class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if set(s) == s or len(set(s)) == 1:
            return len(set(s))
        res = 0
        for i in range(len(s)):
            temp_res = ""
            temp_res += s[i]
            for j in range(i+1,len(s)):
                if s[j] not in temp_res:
                    temp_res += s[j]
                else:
                    break
            res = max(len(temp_res),res)
        return res
