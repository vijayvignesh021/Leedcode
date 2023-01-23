class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = None
        ln =len(nums)
        for i in range(1,ln):
            l,r = i-1,i+1
            while l >= 0 and r < ln :
                tm = nums[l] + nums[i] + nums[r]
                if tm == target:
                    return tm
                elif tm < target:
                    r += 1
                elif tm > target :
                    l -= 1
                if res == None:
                    res = tm
                elif abs(res - target ) > abs(tm - target):
                    res =tm
        return res
