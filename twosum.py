class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return i,j
                elif nums[-(i+1)] + nums[-(j+1)] == target:
                    return (len(nums)-(j+1),len(nums)-(i+1))
