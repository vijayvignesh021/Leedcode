int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    *returnSize = 2;
    int *returnVal = (int*)malloc(2*sizeof(int));
    for(int i =0;i<numsSize-1;i++){
        for(int j =i+1;j<numsSize;j++){
            if(j==i){
                continue;
            }
            else if(nums[i]+nums[j]==target){

                returnVal[0]=i;
                returnVal[1]=j;
            }
                
        }
    }
    return returnVal;

}
