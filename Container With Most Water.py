class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0 , len(height) - 1
        maximum = 0
        while(left < right):
            if height[left] < height[right] :
                maximum = max(maximum , height[left] * (right - left) )
                left += 1
            else : 
                maximum = max(maximum , height[right] * (right - left) )
                right -= 1
        return maximum
