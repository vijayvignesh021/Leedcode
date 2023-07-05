class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
         bool inc = true;
         bool dic = true;
         for(int i = 0 ; i < nums.size() - 1 ; i++){
             if(nums[i] > nums[i+1]){
                 inc = false ;
             }
             if(nums[i] < nums[i+1]){
                 dic = false;
             }
         }
         if (inc || dic){
             return true;
         }
        return false;
    }
};
