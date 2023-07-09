class Solution {
public:
    string toLowerCase(string s) {
        string x ="" ;
        for(int i = 0; i < s.size() ; i++){
            if(s[i] < 91 && s[i] > 64){
            char z = s[i]+32;
                x += z;
            }
            else{
                x += s[i];
            }

        }
        return x;
        
    }
};
