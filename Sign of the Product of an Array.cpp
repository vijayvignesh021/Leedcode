class Solution {
public:
    int arraySign(vector<int>& nums) {
        int  out = 0 ;
        for (int i = 0 ; i < nums.size() ; i++){
            if(nums[i] < 0){
            out += 1;
            }
            if(nums[i] == 0){
                return 0;
            }

        }
        if (out%2  == 0) {
             return 1;
        }
         return -1;

    }
       
};
