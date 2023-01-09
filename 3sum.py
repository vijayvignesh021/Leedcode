class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out =[]
        nums.sort()

        for i , f in enumerate(nums):
            if i>0 and nums[i] == nums[i-1]:
                continue
            lp , rp = i+1,len(nums)-1
            while lp < rp :
                sum = f+nums[lp]+nums[rp]
                if sum >0:
                    rp -=1
                elif sum < 0:
                    lp += 1
                else:
                    out.append([f,nums[lp],nums[rp]])
                    lp += 1
                    while nums[lp] == nums[lp-1] and lp<rp:
                        lp+=1

        return out
