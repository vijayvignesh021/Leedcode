class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        out,out_len,n,m = -1,0,len(needle),len(haystack)
        i,j=0,0
        while(i < n and j < m):

            if needle[i] != haystack[j]:
                out,out_len = -1,0
                j = 1+j-i
                i=0
            else:
                if out == -1:
                    out = j
                out_len+=1
                j+=1
                i+=1
        if out_len !=n:
            return -1
        return out
