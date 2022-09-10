class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = nums1 + nums2
        merge.sort()
        if len(merge)%2 ==0:
            inx = len(merge)//2
            out = (merge[inx-1]+merge[inx])/2
            return float("%.5f"%out)
        else:
            inx = len(merge)//2
            return float("%.5f"%merge[inx])