class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int point1 =0,point2 = 0 ;

        while( point1 <nums.size()){
            if(nums[point1] != 0){
                swap(nums[point1],nums[point2]);
                point2++;
            }

            point1++;
            }
        }
        
};
