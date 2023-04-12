class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        out = []
        for i in range(len(nums)):
            if nums[i] == target:
                out.append(i)
        return out[0],out[-1]
