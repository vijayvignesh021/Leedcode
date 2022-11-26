int removeElement(int* nums, int numsSize, int val){
    int k = numsSize,flg = 0,del = 0;
    for(int i=0;i<numsSize;i++){
        if(flg==0 && nums[i] == val){
            flg = 1;
            del++;
            k--;
        }else if(flg == 1 && nums[i] == val){
            k--;
            del++;
        }else if(nums[i]!=val){
            nums[i-del] = nums[i];
            flg = 0;
        }
    }
    return k;
}
