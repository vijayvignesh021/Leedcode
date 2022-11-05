int search(int* nums, int numsSize, int target){
    int loop = numsSize/2;
    int out = -1;
    int t = 1;
    if(target < nums[loop]){
        t = 0;
    }
    for(loop ; (loop >= 0) && (loop < numsSize);loop){
        if(nums[loop]==target){
            out = loop;
            break;
        }else if(t){

            loop++;
        }else{
            loop--;
            
        }
    }
    return out;

}
