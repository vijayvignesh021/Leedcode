class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out =""
        if len(strs) == 1:
            return strs[0]
        for i in range(1,len(strs)):
            temp = ""
            for j in range(min(len(strs[i-1]),len(strs[i]))):
                if strs[i-1][j] == strs[i][j]:
                    temp += strs[i][j]
                else:
                    break
            strs[i]=temp
            out = temp
        return out
