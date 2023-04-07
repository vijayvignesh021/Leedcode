class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        preinx = { }

        for i , v in enumerate(nums):
            if v in preinx and abs(i-preinx[v]) <= k:
                    return True
            else:
                preinx[v] = i
        return False
