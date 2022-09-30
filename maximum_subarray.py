class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = -999999
        max_end = 0
        for i in range(len(nums)):
            max_end = max_end + nums[i]
            max_so_far=max(max_so_far,max_end)
            if max_end < 0:
                max_end = 0
            
        return max_so_far
