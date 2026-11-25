class Solution:
    def maxArea(self, heights: List[int]) -> int:
        height_len = len(heights)
        i = 0
        j = height_len - 1

        maxArea = 0
        while i < j:
            currentArea = min(heights[i], heights[j]) * (j - i)
            if (maxArea < currentArea):
                maxArea = currentArea
            if heights[i] <= heights[j]:
                i+=1
            else:
                j-=1 

        return maxArea
            
