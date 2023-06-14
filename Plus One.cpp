class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {

        int carry = 1;
        for(int n = digits.size()-1; n >= 0 ; n--){
            int x = digits[n] + carry;
            digits[n] = x % 10;
            carry = x / 10;
        }
        if(carry){
            digits.insert(digits.begin(),carry);
        }
        return digits;
        
    }
};
