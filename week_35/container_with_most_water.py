class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        maximum = float("-inf")

        while left < right:
            water_contained = min(height[left], height[right]) * (right - left)
            maximum = max(maximum, water_contained)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return maximum