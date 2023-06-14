class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int n=s.size();
        for(int i=n/2;i>=1;i--){ 
            cout<< s.substr(i) << " " << s.substr(0,n-i) <<" "<<n<<i;
            if(n%i==0){
                cout<< endl << "new" ;
                 if(s.substr(0,n-i)==s.substr(i))return true;         
            }
        }
        return false;
    }
};
