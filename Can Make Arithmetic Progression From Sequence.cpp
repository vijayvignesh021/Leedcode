class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        int n =arr.size();
        sort(arr.begin(),arr.end());
        int per_diff = arr [0] - arr[1];
        for (int i = 1 ; i < n ; i++){
            if(arr[i-1] - arr[i] != per_diff){
                return false;
            }
        }
        return true;
    }
};
