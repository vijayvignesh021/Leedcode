class Solution {
public:
    int strStr(string haystack, string needle) {
        int index_out , i = 0;
        int j = 0;
        while ( i < haystack.length()){
            if(haystack[i] == needle[j]){
                if (j == needle.length()-1){
                    return i-j;
                }
                j++;
            }
            else{
                i = i-j;
                j = 0;
            }
            i++;
        }
        return -1;
        
    }
};
