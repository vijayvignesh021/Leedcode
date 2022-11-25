int removeDuplicates(int* nums, int numsSize){
    int k=0;
    int store;
    for(int i=0;i<numsSize;++i){
        if(i==0 || nums[i]!=store){
            store = nums[i];
            nums[k]=nums[i];
            k++;
        }
    }
     return k ;
}
